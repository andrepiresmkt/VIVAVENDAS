# organizar_imagens.py
# Copia todas as imagens do Google Drive (CONVIVA MKT ESPELHO)
# para viva-vendas/img/empreendimentos/ organizado por pasta de projeto.
#
# Rodar no PowerShell:
#   cd "C:\Users\andre\OneDrive\Documentos\viva-vendas"
#   python organizar_imagens.py

import os, shutil, sys
from pathlib import Path

# ── Configuracao ──────────────────────────────────────────────────────────────
DRIVE_ROOT = Path(r"G:\Meu Drive\CONVIVA MKT ESPELHO")
DEST_ROOT  = Path(r"C:\Users\andre\OneDrive\Documentos\viva-vendas\img\empreendimentos")

EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.tiff', '.tif', '.bmp', '.heic', '.avif'}

# ── Diagnóstico: mostra o que existe em G:\ ───────────────────────────────────
g = Path("G:\\")
if g.exists():
    print("\nConteudo de G:\\")
    for item in sorted(g.iterdir()):
        print(f"  {'[D]' if item.is_dir() else '[F]'}  {item.name}")
    print()

meu_drive = Path(r"G:\Meu Drive")
if meu_drive.exists():
    print("Conteudo de G:\\Meu Drive\\")
    for item in sorted(meu_drive.iterdir()):
        print(f"  {'[D]' if item.is_dir() else '[F]'}  {item.name}")
    print()

# ── Verificacao ───────────────────────────────────────────────────────────────
if not DRIVE_ROOT.exists():
    print(f"\nERRO: pasta nao encontrada: {DRIVE_ROOT}")
    print("Verifique se o Google Drive esta sincronizado e o caminho esta correto.")
    sys.exit(1)

# Conta arquivos reais vs placeholders (Google Drive streaming = tamanho 0)
all_files = list(DRIVE_ROOT.rglob("*"))
real = [f for f in all_files if f.is_file() and f.stat().st_size > 0]
placeholder = [f for f in all_files if f.is_file() and f.stat().st_size == 0]
print(f"Arquivos na pasta fonte: {len(real)} reais, {len(placeholder)} placeholders (nao baixados)")
if placeholder and not real:
    print("\n  ATENCAO: Todos os arquivos sao placeholders do Google Drive.")
    print("  Solucao: Abra o Google Drive no Explorer, selecione a pasta")
    print("  'CONVIVA MKT ESPELHO', clique direito → 'Disponibilizar offline'")
    print("  e aguarde o download. Depois rode este script novamente.\n")
    sys.exit(1)

DEST_ROOT.mkdir(parents=True, exist_ok=True)

# ── Primeiro passe: inventario ────────────────────────────────────────────────
print(f"\n{'─'*60}")
print(f"  FONTE : {DRIVE_ROOT}")
print(f"  DESTINO: {DEST_ROOT}")
print(f"{'─'*60}\n")

print("Escaneando pastas...\n")
inventory = {}  # pasta_nome -> lista de Path de imagens

for dirpath, dirnames, filenames in os.walk(DRIVE_ROOT):
    dirnames.sort()
    imgs = [
        Path(dirpath) / f
        for f in sorted(filenames)
        if Path(f).suffix.lower() in EXTS
    ]
    if imgs:
        rel = Path(dirpath).relative_to(DRIVE_ROOT)
        key = str(rel) if str(rel) != '.' else '_raiz'
        inventory[key] = imgs

if not inventory:
    print("Nenhuma imagem encontrada. Verifique se o Drive esta sincronizado.")
    sys.exit(1)

total_src = sum(len(v) for v in inventory.values())
print(f"Encontradas {total_src} imagens em {len(inventory)} pasta(s):\n")
for folder, imgs in inventory.items():
    print(f"  [{len(imgs):3d}]  {folder}")

print(f"\n{'─'*60}")
resp = input("Copiar tudo? (s/n): ").strip().lower()
if resp != 's':
    print("Cancelado.")
    sys.exit(0)

# ── Segundo passe: copia ──────────────────────────────────────────────────────
print()
copied = skipped = errors = 0

for folder, imgs in inventory.items():
    # Limpa o nome da pasta para usar como diretorio de destino
    safe = folder.replace('\\', os.sep).replace('/', os.sep)
    dest_dir = DEST_ROOT / safe
    dest_dir.mkdir(parents=True, exist_ok=True)

    for src in imgs:
        dest = dest_dir / src.name
        if dest.exists():
            skipped += 1
            continue
        try:
            shutil.copy2(src, dest)
            copied += 1
        except Exception as e:
            print(f"  ERRO ao copiar {src.name}: {e}")
            errors += 1

    print(f"  ✓  {folder}  ({len(imgs)} imagens)")

# ── Relatorio final ───────────────────────────────────────────────────────────
print(f"\n{'─'*60}")
print(f"  Copiadas : {copied}")
print(f"  Ja existiam (skip): {skipped}")
print(f"  Erros    : {errors}")
print(f"{'─'*60}")
print(f"\nImagens em: {DEST_ROOT}\n")

# ── Gera lista de pastas criadas para referencia ──────────────────────────────
lista_path = DEST_ROOT / '_inventario.txt'
with open(lista_path, 'w', encoding='utf-8') as f:
    f.write(f"INVENTARIO DE IMAGENS - CONVIVA MKT\n")
    f.write(f"Gerado automaticamente por organizar_imagens.py\n\n")
    for folder, imgs in inventory.items():
        f.write(f"\n[{folder}]  ({len(imgs)} imagens)\n")
        for img in imgs:
            kb = img.stat().st_size // 1024
            f.write(f"  {img.name}  ({kb} KB)\n")

print(f"Inventario salvo em: {lista_path}\n")
