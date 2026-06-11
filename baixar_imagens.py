# baixar_imagens.py
# Baixa todas as imagens do WordPress CDN para img/wp/
# e atualiza todos os HTMLs para usar caminhos locais.
#
# Rodar no PowerShell:
#   cd viva-vendas
#   python baixar_imagens.py
import os, re, glob, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
WP_DIR   = os.path.join(ROOT, 'img', 'wp')
THUMB_DIR = os.path.join(WP_DIR, 'thumbs')
os.makedirs(WP_DIR,   exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)

BASE = 'https://convivaengenharia.com.br/wp-content/uploads'

# ── Mapeamento: URL remota → arquivo local ────────────────────────────────────
IMAGES = {
    # 2025/04
    f'{BASE}/2025/04/FF55-COL-01-Tipo-Suite-scaled.jpg':
        os.path.join(WP_DIR, 'FF55-COL-01-Tipo-Suite-scaled.jpg'),
    f'{BASE}/2025/04/FF55-COL-04-Tipo-Sala-scaled.jpg':
        os.path.join(WP_DIR, 'FF55-COL-04-Tipo-Sala-scaled.jpg'),
    f'{BASE}/2025/04/FF55-Rooftop-Area-gourmet-Vista-01-scaled.jpg':
        os.path.join(WP_DIR, 'FF55-Rooftop-Area-gourmet-Vista-01-scaled.jpg'),
    f'{BASE}/2025/04/FF55-Rooftop-Piscina-Vista-01-scaled.jpg':
        os.path.join(WP_DIR, 'FF55-Rooftop-Piscina-Vista-01-scaled.jpg'),
    f'{BASE}/2025/04/FF55-Rooftop-Piscina-Vista-02-1-scaled.jpg':
        os.path.join(WP_DIR, 'FF55-Rooftop-Piscina-Vista-02-1-scaled.jpg'),
    f'{BASE}/2025/04/Fachada-scaled.jpeg':
        os.path.join(WP_DIR, 'Fachada-scaled.jpeg'),
    f'{BASE}/2025/04/Life-Inga-Apartamento-01-Sala-de-estar-2qt-scaled.jpg':
        os.path.join(WP_DIR, 'Life-Inga-Apartamento-01-Sala-de-estar-2qt-scaled.jpg'),
    f'{BASE}/2025/04/Life-Inga-Apartamento-05-Quarto-1qt-scaled.jpg':
        os.path.join(WP_DIR, 'Life-Inga-Apartamento-05-Quarto-1qt-scaled.jpg'),
    f'{BASE}/2025/04/Life-Inga-Apartamento-05-Sala-1qt-scaled.jpg':
        os.path.join(WP_DIR, 'Life-Inga-Apartamento-05-Sala-1qt-scaled.jpg'),
    f'{BASE}/2025/04/Life-Inga-Apartamento-07-Cozinha-scaled.jpg':
        os.path.join(WP_DIR, 'Life-Inga-Apartamento-07-Cozinha-scaled.jpg'),
    f'{BASE}/2025/04/Life-Inga-Apartamento-07-Quarto-scaled.jpg':
        os.path.join(WP_DIR, 'Life-Inga-Apartamento-07-Quarto-scaled.jpg'),
    f'{BASE}/2025/04/Life-Inga-Bicicletario-scaled.jpg':
        os.path.join(WP_DIR, 'Life-Inga-Bicicletario-scaled.jpg'),
    f'{BASE}/2025/04/Life-Inga-Delivery-scaled.jpg':
        os.path.join(WP_DIR, 'Life-Inga-Delivery-scaled.jpg'),
    f'{BASE}/2025/04/Life-Inga-Hall-de-entrada-scaled.jpg':
        os.path.join(WP_DIR, 'Life-Inga-Hall-de-entrada-scaled.jpg'),
    f'{BASE}/2025/04/Life-Inga-Minimarket-scaled.jpg':
        os.path.join(WP_DIR, 'Life-Inga-Minimarket-scaled.jpg'),
    f'{BASE}/2025/04/2-quartos-com-varanda.png':
        os.path.join(WP_DIR, '2-quartos-com-varanda.png'),
    f'{BASE}/2025/04/Studio-com-varanda.png':
        os.path.join(WP_DIR, 'Studio-com-varanda.png'),
    # 2025/05
    f'{BASE}/2025/05/PauloAlves-03-alta.jpg':
        os.path.join(WP_DIR, 'PauloAlves-03-alta.jpg'),
    # elementor/thumbs → local thumbs/ (nomes simplificados)
    f'{BASE}/elementor/thumbs/02-CONVIVA-MB_FACHADA-21-rfuy0tuxstq8eme6wknhcgdl7qa6mi8wq20u86qh6q.jpg':
        os.path.join(THUMB_DIR, '02-CONVIVA-MB_FACHADA-21.jpg'),
    f'{BASE}/elementor/thumbs/CONVIVA-Site-Life-Camboinhas-Perspectivas-Prancheta-1-scaled-r3nh2pmk1n2ullizx6818yal8016nuvpawqb18awle.webp':
        os.path.join(THUMB_DIR, 'Life-Camboinhas-Perspectivas.webp'),
    f'{BASE}/elementor/thumbs/Camboinhas-Perspectiva-22-r52qjhmohy0pcaefsu2ydv2mclm02ka7ifg249tvuq.jpg':
        os.path.join(THUMB_DIR, 'Camboinhas-Perspectiva-22.jpg'),
    f'{BASE}/elementor/thumbs/Inga-Fitness-v06-13-01-2023_4000-1-scaled-r52qjhmohy0pcaefsu2ydv2mclm02ka7ifg249tvuq.jpg':
        os.path.join(THUMB_DIR, 'Inga-Fitness.jpg'),
    f'{BASE}/elementor/thumbs/Sala-406-scaled-r52qjfr049y4p2h63t9p8vjp5tv9n62qu6535pwo76.jpg':
        os.path.join(THUMB_DIR, 'Sala-406.jpg'),
}

# ── STEP 1: Baixar ────────────────────────────────────────────────────────────
print('\n─── BAIXANDO IMAGENS ───────────────────────────────')
headers = {'User-Agent': 'Mozilla/5.0 (compatible; VivaBotDownloader/1.0)'}
ok, skip, fail = 0, 0, 0

for url, dest in IMAGES.items():
    if os.path.exists(dest):
        print(f'  skip  {os.path.basename(dest)}')
        skip += 1
        continue
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        size = os.path.getsize(dest)
        print(f'  ✓     {os.path.basename(dest):55s} ({size//1024} KB)')
        ok += 1
    except Exception as e:
        print(f'  ✗     {os.path.basename(dest)} → {e}')
        fail += 1

print(f'\n  Baixados: {ok}  |  Já existiam: {skip}  |  Falhas: {fail}')

if fail > 0:
    print('\n  ⚠  Algumas imagens falharam. Verifique sua conexão e tente novamente.')
    raise SystemExit(1)

# ── STEP 2: Atualizar HTMLs ────────────────────────────────────────────────────
print('\n─── ATUALIZANDO HTMLS ──────────────────────────────')

def get_local_path(url: str, html_path: str) -> str:
    """Retorna o caminho relativo correto de dest_local para o HTML."""
    dest = IMAGES[url]
    html_dir = os.path.dirname(html_path)
    rel = os.path.relpath(dest, html_dir).replace('\\', '/')
    return rel

all_htmls = (
    glob.glob(os.path.join(ROOT, '*.html')) +
    glob.glob(os.path.join(ROOT, 'imoveis', '*.html')) +
    glob.glob(os.path.join(ROOT, 'bairros', '*.html'))
)

total_replaced = 0
for html_path in sorted(all_htmls):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for url in IMAGES:
        if url in content:
            local = get_local_path(url, html_path)
            content = content.replace(url, local)

    replaced = content.count('img/wp') - original.count('img/wp')
    if content != original:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        rel = os.path.relpath(html_path, ROOT)
        print(f'  ✓  {rel}')
        total_replaced += 1

if total_replaced == 0:
    print('  (nenhum HTML precisava de atualização)')
else:
    print(f'\n  {total_replaced} arquivo(s) atualizado(s).')

# ── STEP 3: Verificação final ─────────────────────────────────────────────────
print('\n─── VERIFICAÇÃO FINAL ──────────────────────────────')
remaining = 0
for html_path in all_htmls:
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    count = content.count('convivaengenharia.com.br/wp-content/uploads')
    if count:
        print(f'  ⚠  {os.path.relpath(html_path, ROOT)}: {count} URL(s) remota(s) ainda')
        remaining += count

if remaining == 0:
    print('  ✓  Zero URLs remotas do WordPress nos HTMLs. Tudo local!')
else:
    print(f'\n  ⚠  {remaining} URL(s) remota(s) restante(s) — verifique acima.')

print('\n─── CONCLUÍDO ──────────────────────────────────────\n')
