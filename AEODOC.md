# AEODOC — Plano Completo de Answer Engine Optimization
## Viva Vendas · Niterói · Mercado Imobiliário
> Versão 1.0 · Junho 2026 · Referência: Ahrefs AEO Guide 2025

---

## O QUE É AEO E POR QUE IMPORTA PARA IMÓVEIS

AEO (Answer Engine Optimization) é a prática de estruturar seu site para que **Perplexity, ChatGPT, Google AI Overviews, Gemini e assistentes de voz** citem seu conteúdo diretamente nas respostas — sem o usuário precisar clicar em nada.

No mercado imobiliário, isso é ouro: quando alguém pergunta ao ChatGPT "onde comprar apartamento perto da praia em Niterói?", o site que responder de forma mais clara, estruturada e confiável é citado. Viva Vendas pode ser essa resposta.

**Diferença AEO vs SEO tradicional:**

| | AEO | SEO |
|---|---|---|
| Meta | Ser *citado* em respostas de IA | Ranquear em resultados de busca |
| Conteúdo | Respostas diretas e declarativas | Páginas longas para ranking |
| Queries | Perguntas conversacionais | Keywords de volume alto |
| Técnico | Schema, crawlabilidade, sem JS pesado | Meta tags, headings, backlinks |
| Medição | Citações em IA, menções de marca | Cliques, impressões, posição |

**Timeline realista para site novo:** 6–12 meses para primeiras citações consistentes. Mas as ações técnicas têm efeito imediato assim que o Google indexar.

---

## AUDITORIA ATUAL — BASELINE (Junho 2026)

### Pontuação por categoria

| Categoria | Status | Nota |
|---|---|---|
| Schema markup geral | 21/23 páginas | 8/10 |
| FAQPage schema | 9/23 páginas | 4/10 |
| H1 semântico | 3/23 páginas | **1/10** |
| Open Graph | 0/23 páginas | **0/10** |
| BreadcrumbList | 4/23 páginas | 2/10 |
| GeoCoordinates | 5/23 páginas | 2/10 |
| HowTo schema | 0/23 páginas | **0/10** |
| Speakable schema | 0/23 páginas | **0/10** |
| Person/Author schema | 0/23 páginas | **0/10** |
| Meta description | 22/23 páginas | 9/10 |
| Canonical URL | 22/23 páginas | 9/10 |
| Sitemap.xml indexado | Não submetido | 3/10 |
| Conteúdo Q&A | Parcial | 4/10 |
| NAP consistente | Inconsistente | 3/10 |
| Conteúdo comparativo | 1 página | 2/10 |

### **Nota geral AEO atual: 5,5 / 10**

### Páginas sem H1 (crítico — 20 de 23)
Todas exceto `calculadora.html`, `comparativo.html`, `obrigado.html`.

### Páginas sem FAQ (perda de citação direta — 13 de 23)
`comparativo.html`, `conviva.html`, `equipe.html`, `financiamento.html`, `sobre.html`, `tabela-precos.html`, todos os 7 de `imoveis/`.

---

## PLANO DE ATAQUE — FASES E PRIORIDADES

---

### FASE 1 — FUNDAÇÃO TÉCNICA (impacto imediato)
> Prazo: 1–2 semanas · Sem produção de conteúdo

#### 1.1 · H1 Semântico em Todas as Páginas

O `<h1>` é o sinal principal que IA usa para entender do que a página se trata. Sem ele, a página é "sem título" para motores de resposta.

**Regras de implementação:**
- Um único `<h1>` por página
- Deve conter a keyword principal + localização quando relevante
- Visualmente pode ser `opacity: 0; position: absolute; height: 0;` se não couber no design (H1 oculto válido para SEO, não para acessibilidade — preferível integrá-lo ao design)
- Melhor prática: integrar como parte visual do hero ou header da seção principal

**H1s definidos por página:**

```
index.html           → "Apartamentos à Venda em Niterói — Viva Vendas"
investir.html        → "Por que Investir em Imóveis em Niterói?"
calculadora.html     → "Calculadora de Rentabilidade Imobiliária — Niterói"
equipe.html          → "Corretores de Imóveis em Niterói — Equipe Viva Vendas"
conviva.html         → "Conviva Engenharia — Construtora em Niterói"
sobre.html           → "Sobre a Viva Vendas — Consultoria Imobiliária em Niterói"
financiamento.html   → "Financiamento Imobiliário em Niterói — Como Funciona"
fgts.html            → "Como Usar o FGTS para Comprar Apartamento em Niterói"
aluguel-temporada.html → "Aluguel por Temporada em Niterói — Rentabilidade e Dicas"
tabela-precos.html   → "Tabela de Preços — Empreendimentos Conviva em Niterói"
comparativo.html     → "Comparativo de Empreendimentos Conviva em Niterói"
bairros/camboinhas.html  → "Apartamentos à Venda em Camboinhas, Niterói"
bairros/icarai.html      → "Apartamentos à Venda no Icaraí, Niterói"
bairros/inga.html        → "Apartamentos à Venda no Ingá, Niterói"
bairros/piratininga.html → "Apartamentos à Venda em Piratininga, Niterói"
imoveis/brise.html       → "Conviva Brise — Apartamentos em Camboinhas, Niterói"
imoveis/camboinhas.html  → "Conviva Camboinhas — Empreendimento à Beira-Mar"
imoveis/icarai.html      → "Conviva Icaraí Imparato — Apartamentos no Icaraí"
imoveis/inga.html        → "Conviva Ingá — Lançamento Imobiliário em Niterói"
imoveis/life-camboinhas.html → "Life Camboinhas — Apartamentos na Praia de Camboinhas"
imoveis/life-inga.html   → "Life Ingá — Lançamento Conviva no Ingá, Niterói"
imoveis/piratininga.html → "Conviva Piratininga — Apartamentos à Beira-Mar"
```

---

#### 1.2 · Open Graph em Todas as Páginas

Open Graph afeta como o site aparece quando linkado no WhatsApp, Instagram, LinkedIn e é lido por crawlers de redes sociais que alimentam modelos de linguagem.

**Bloco padrão a inserir no `<head>` de cada página:**

```html
<meta property="og:type" content="website">
<meta property="og:site_name" content="Viva Vendas">
<meta property="og:title" content="[título da página]">
<meta property="og:description" content="[meta description existente]">
<meta property="og:url" content="https://vivavendas.com.br/[slug]">
<meta property="og:image" content="https://vivavendas.com.br/img/og-cover.jpg">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[título da página]">
<meta name="twitter:description" content="[meta description existente]">
<meta name="twitter:image" content="https://vivavendas.com.br/img/og-cover.jpg">
```

**Imagem OG:** Criar `img/og-cover.jpg` (1200×630px) com foto de Camboinhas + logo Viva Vendas. Será usada como fallback em todas as páginas. Páginas de imóveis específicos podem ter OG image própria.

---

#### 1.3 · RealEstateAgent Schema Completo no Index

O schema atual no `index.html` é básico. Expandir para incluir todos os campos que LLMs usam para construir entidade de marca:

```json
{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "@id": "https://vivavendas.com.br/#organization",
  "name": "Viva Vendas",
  "alternateName": "Viva Vendas Consultoria Imobiliária",
  "description": "Consultoria imobiliária exclusiva nos empreendimentos Conviva Engenharia em Niterói. Especialistas em Camboinhas, Icaraí, Ingá e Piratininga.",
  "url": "https://vivavendas.com.br",
  "telephone": "+55-21-96703-1691",
  "email": "contato@vivavendas.com.br",
  "foundingDate": "2023",
  "areaServed": [
    {"@type": "City", "name": "Niterói", "sameAs": "https://www.wikidata.org/wiki/Q174762"},
    {"@type": "Neighborhood", "name": "Camboinhas"},
    {"@type": "Neighborhood", "name": "Icaraí"},
    {"@type": "Neighborhood", "name": "Ingá"},
    {"@type": "Neighborhood", "name": "Piratininga"}
  ],
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Niterói",
    "addressRegion": "RJ",
    "addressCountry": "BR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": -22.8838,
    "longitude": -43.1030
  },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Empreendimentos Conviva em Niterói",
    "itemListElement": [
      {"@type": "Offer", "name": "Conviva Brise", "description": "Studios e apartamentos em Camboinhas"},
      {"@type": "Offer", "name": "Life Camboinhas", "description": "Apartamentos à beira-mar em Camboinhas"},
      {"@type": "Offer", "name": "Conviva Icaraí Imparato", "description": "Apartamentos no Icaraí"},
      {"@type": "Offer", "name": "Life Ingá", "description": "Lançamento no Ingá, Niterói"},
      {"@type": "Offer", "name": "Conviva Piratininga", "description": "Apartamentos em Piratininga"}
    ]
  },
  "sameAs": [
    "https://www.instagram.com/vivavendas.niteroi",
    "https://www.facebook.com/vivavendas",
    "https://business.google.com/vivavendas"
  ],
  "knowsAbout": [
    "Imóveis em Niterói",
    "Empreendimentos Conviva Engenharia",
    "Investimento imobiliário em Niterói",
    "Apartamentos à beira-mar",
    "FGTS para compra de imóvel",
    "Financiamento imobiliário",
    "Aluguel por temporada em Niterói"
  ]
}
```

---

#### 1.4 · Person Schema para Cada Corretor (equipe.html)

LLMs usam `Person` schema para entender quem são os especialistas por trás da marca. Isso alimenta E-E-A-T (Experience, Expertise, Authoritativeness, Trust).

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "André [Sobrenome]",
  "jobTitle": "Corretor de Imóveis",
  "hasCredential": {
    "@type": "EducationalOccupationalCredential",
    "name": "CRECI-RJ",
    "credentialCategory": "license"
  },
  "worksFor": {"@id": "https://vivavendas.com.br/#organization"},
  "areaServed": "Niterói, RJ",
  "knowsAbout": ["Empreendimentos Conviva", "Investimento imobiliário", "Camboinhas", "Icaraí"],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+55-21-96703-1691",
    "contactType": "sales"
  }
}
```

Repetir para cada corretor com seus campos específicos (`knowsAbout` varia por especialidade).

---

#### 1.5 · BreadcrumbList em Todas as Páginas de Profundidade

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://vivavendas.com.br"},
    {"@type": "ListItem", "position": 2, "name": "Bairros", "item": "https://vivavendas.com.br/bairros/"},
    {"@type": "ListItem", "position": 3, "name": "Camboinhas", "item": "https://vivavendas.com.br/bairros/camboinhas"}
  ]
}
```

Adaptar para cada nível: `bairros/`, `imoveis/`.

---

#### 1.6 · GeoCoordinates em Todas as Páginas de Bairro e Imóvel

Coordenadas específicas por localização aumentam citação em buscas com intenção geográfica ("perto de mim", "na praia").

```
Camboinhas:   -22.9642, -43.0541
Icaraí:       -22.9002, -43.1204
Ingá:         -22.9072, -43.1271
Piratininga:  -22.9731, -43.0621
```

---

#### 1.7 · Sitemap.xml Linkado no `<head>`

Adicionar em todas as páginas, dentro do `<head>`:
```html
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
```

E adicionar no arquivo `sitemap.xml` as datas de modificação (`<lastmod>`) e prioridades (`<priority>`) corretas.

---

#### 1.8 · NAP — Name, Address, Phone Consistente

Motores de resposta verificam consistência de NAP em todas as menções. Definir e usar **exatamente** assim em todo o site e em plataformas externas:

```
Nome:     Viva Vendas
Telefone: (21) 96703-1691
Cidade:   Niterói, RJ
URL:      https://vivavendas.com.br
```

Verificar e padronizar no rodapé de todas as 23 páginas.

---

### FASE 2 — SCHEMA AVANÇADO (alto impacto em citação)
> Prazo: 2–4 semanas

#### 2.1 · FAQPage Schema em Todas as Páginas com FAQ HTML

Páginas que já têm perguntas em HTML mas não têm schema: `calculadora.html`, e todas as `imoveis/`.

Adicionar FAQPage schema sempre que houver seção de perguntas — é o tipo mais citado por AI Overviews em queries informacionais.

**Template:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Qual o preço do m² em Camboinhas?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "O preço médio do m² em Camboinhas em 2025 varia entre R$ 8.500 e R$ 12.000 para empreendimentos novos, dependendo da metragem e do andar. Studios a partir de R$ 380.000."
      }
    }
  ]
}
```

---

#### 2.2 · HowTo Schema (nenhuma página tem — vantagem competitiva)

HowTo é exibido como passo a passo em AI Overviews. Nenhum concorrente regional usa isso. Candidatos:

**`fgts.html`** — "Como usar FGTS para comprar apartamento":
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Como usar o FGTS para comprar apartamento em Niterói",
  "totalTime": "PT30D",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Verifique seu saldo FGTS",
      "text": "Acesse o app FGTS (Caixa Econômica Federal) ou o site fgts.caixa.gov.br para consultar seu saldo disponível."
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "Confirme o tempo de contribuição",
      "text": "Você precisa de pelo menos 3 anos de contribuição ao FGTS (podendo ser em empregos diferentes) para usar na compra do primeiro imóvel."
    },
    {
      "@type": "HowToStep",
      "position": 3,
      "name": "Escolha o imóvel dentro do limite",
      "text": "No Rio de Janeiro, o imóvel financiado pelo SFH deve ter valor de avaliação de até R$ 1,5 milhão. Os empreendimentos Conviva em Niterói se enquadram nesse limite."
    },
    {
      "@type": "HowToStep",
      "position": 4,
      "name": "Solicite a liberação com o corretor",
      "text": "Nosso corretor coordena toda a documentação junto ao banco. O processo de liberação do FGTS leva em média 15 a 30 dias."
    }
  ]
}
```

**`financiamento.html`** — "Como financiar um apartamento em Niterói":
Steps: Simule, escolha o banco, reúna documentação, assine contrato, aguarde liberação.

**`calculadora.html`** — "Como calcular a rentabilidade de um imóvel":
Steps: Insira o valor do imóvel, informe o aluguel esperado, veja o cap rate, compare com investimentos alternativos.

---

#### 2.3 · Speakable Schema (zero concorrentes usam)

`speakable` marca os trechos mais importantes para leitura por assistentes de voz (Google Assistant, Alexa). É um sinal de confiança para IA.

**Adicionar em index.html, investir.html e páginas de bairro:**
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".hero-headline", ".section-intro", ".faq-a"]
  },
  "url": "https://vivavendas.com.br"
}
```

O seletor `.faq-a` marca as respostas das FAQs como "faláveis" — ideal para queries de voz como "Ok Google, qual o preço de apartamento em Camboinhas?".

---

#### 2.4 · Apartment / RealEstateListing Schema nas Páginas de Imóveis

Cada página `imoveis/` deve ter schema do tipo `Apartment` ou `Product` descrevendo o empreendimento:

```json
{
  "@context": "https://schema.org",
  "@type": "Apartment",
  "name": "Conviva Brise",
  "description": "Studios e apartamentos de 1 e 2 quartos em Camboinhas, Niterói. À 200m da praia.",
  "numberOfRooms": "1-3",
  "floorSize": {"@type": "QuantitativeValue", "value": 35, "unitCode": "MTK"},
  "petsAllowed": true,
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Camboinhas",
    "addressLocality": "Niterói",
    "addressRegion": "RJ",
    "addressCountry": "BR"
  },
  "geo": {"@type": "GeoCoordinates", "latitude": -22.9642, "longitude": -43.0541},
  "offers": {
    "@type": "Offer",
    "priceCurrency": "BRL",
    "price": "380000",
    "availability": "https://schema.org/InStock",
    "seller": {"@id": "https://vivavendas.com.br/#organization"}
  }
}
```

---

#### 2.5 · Article Schema nas Páginas de Conteúdo Informacional

Páginas como `investir.html`, `fgts.html`, `financiamento.html`, `aluguel-temporada.html` devem ter `Article` schema, transformando-as em fontes cítaveis:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Por que Investir em Imóveis em Niterói em 2025?",
  "datePublished": "2025-01-01",
  "dateModified": "2026-06-01",
  "author": {
    "@type": "Organization",
    "@id": "https://vivavendas.com.br/#organization"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Viva Vendas",
    "logo": {
      "@type": "ImageObject",
      "url": "https://vivavendas.com.br/img/logo.svg"
    }
  },
  "mainEntityOfPage": "https://vivavendas.com.br/investir"
}
```

---

### FASE 3 — CONTEÚDO AEO (onde a guerra é vencida)
> Prazo: 4–12 semanas · Maior impacto a longo prazo

Esta é a fase mais importante. Schema sem conteúdo é casca vazia. LLMs citam sites que **respondem perguntas específicas melhor do que qualquer outro**.

#### 3.1 · Banco de Perguntas — Queries que Viva Vendas Deve Dominar

Estas são as perguntas que usuários fazem a IAs sobre imóveis em Niterói. Cada uma deve ter resposta clara e declarativa no site:

**Perguntas de preço (alta citabilidade):**
- Qual o preço do m² em Camboinhas?
- Quanto custa um studio em Niterói?
- Qual o preço de apartamento na praia em Niterói?
- Qual o valor do m² no Icaraí?
- Apartamento em Piratininga quanto custa?

**Perguntas de investimento:**
- Vale a pena comprar apartamento em Niterói para investir?
- Qual a rentabilidade de aluguel por temporada em Camboinhas?
- Qual o retorno do investimento imobiliário em Niterói?
- Niterói ou Rio de Janeiro — onde investir em imóveis?
- Conviva Engenharia entrega no prazo?

**Perguntas sobre bairros:**
- Qual o melhor bairro de Niterói para morar perto da praia?
- Camboinhas ou Piratininga — qual é melhor?
- Como é morar em Camboinhas?
- Quanto tempo leva de Niterói para o Rio de Janeiro?
- Camboinhas fica longe do centro de Niterói?

**Perguntas sobre processo de compra:**
- Posso usar FGTS para comprar apartamento na planta em Niterói?
- Como funciona o financiamento de um apartamento Conviva?
- Quais documentos preciso para comprar um apartamento em Niterói?
- Quanto de entrada preciso para comprar apartamento em Niterói?
- O que é Minha Casa Minha Vida e se aplica a empreendimentos Conviva?

**Perguntas sobre Conviva Engenharia:**
- Conviva Engenharia é confiável?
- Quais empreendimentos a Conviva Engenharia tem em Niterói?
- Conviva Brise quando entrega?
- Life Camboinhas fica onde?
- Qual a diferença entre Conviva Brise e Life Camboinhas?

---

#### 3.2 · Estrutura de Resposta AEO-Ready

Todo bloco de conteúdo deve seguir este padrão para maximizar citação:

```
[Heading = a pergunta]
[Parágrafo 1 = resposta direta, 2–3 frases declarativas, sem enrolação]
[Parágrafo 2 = contexto, dados, números concretos]
[Parágrafo 3 = call-to-action soft]
```

**Exemplo correto:**
> **Qual o preço do m² em Camboinhas?**
> O preço médio do m² em Camboinhas, Niterói, está entre R$ 9.000 e R$ 11.500 para empreendimentos novos (2025). Studios com 35 m² partem de R$ 380.000 e apartamentos de 2 quartos chegam a R$ 750.000.
> A valorização de Camboinhas foi de 10,6% ao ano nos últimos 3 anos — acima da média nacional e da cidade do Rio de Janeiro — impulsionada pela escassez de terrenos à beira-mar e pelo perfil premium dos empreendimentos Conviva Engenharia.
> *Veja as opções disponíveis no Conviva Brise e Life Camboinhas ou fale com um corretor para valores atualizados.*

**Exemplo errado (IA não cita):**
> "Camboinhas é um lugar incrível! Venha conhecer nossos apartamentos exclusivos à beira-mar. Entre em contato!"

---

#### 3.3 · Páginas de Conteúdo Novas a Criar

Cada página abaixo responde um cluster de perguntas que hoje não existe no site:

**P1 — `blog/preco-m2-niteroi.html`**
"Preço do m² em Niterói por bairro — Guia 2025"
Tabela com Camboinhas, Icaraí, Ingá, Piratininga, Pendotiba. Dados, gráfico de valorização, comparativo com Rio.

**P2 — `blog/camboinhas-vs-piratininga.html`**
"Camboinhas ou Piratininga: qual bairro escolher?"
Comparativo direto: preço, distância do centro, perfil de morador, potencial de locação, empreendimentos disponíveis.

**P3 — `blog/retorno-aluguel-temporada-niteroi.html`**
"Retorno do aluguel por temporada em Niterói — quanto rende?"
Dados concretos de diária média, taxa de ocupação, cap rate anualizado por bairro.

**P4 — `blog/conviva-engenharia-historico.html`**
"Conviva Engenharia: histórico, entregas e empreendimentos em Niterói"
VGV entregue, número de unidades, prêmios, pontualidade de entrega. Fonte de autoridade sobre a construtora.

**P5 — `blog/financiamento-apartamento-planta.html`**
"Como financiar apartamento na planta — passo a passo"
HowTo schema completo. Alta chance de aparecer como featured snippet e AI Overview.

**P6 — `blog/niteroi-rio-comparativo-investimento.html`**
"Niterói x Rio de Janeiro: onde é melhor investir em imóveis?"
Valorização, custo por m², infraestrutura, qualidade de vida. Posicionamento como referência em análise imobiliária.

**P7 — `faq/index.html`** — Hub Central de Perguntas
Página com 30–50 perguntas agrupadas por tema. FAQPage schema completo. Âncora para todo o conteúdo do site.

---

#### 3.4 · Upgrade de Conteúdo nas Páginas Existentes

**`bairros/camboinhas.html` — `bairros/icarai.html` — etc.**
Adicionar seção "Perguntas frequentes sobre [bairro]" com respostas de pelo menos 3 parágrafos cada. Hoje as respostas são de 1–2 linhas — curtas demais para citação.

**`investir.html`**
Adicionar dados quantitativos: "valorização de X% ao ano", "rentabilidade de Y% a.a. em aluguel por temporada", "Niterói superou o Rio em Z% em valorização". LLMs adoram números.

**`imoveis/brise.html` — etc.**
Cada página de empreendimento deve ter: preço por m², metragem disponível, prazo de entrega, diferenciais concretos (não apenas "luxo e conforto"), e seção FAQ do empreendimento.

---

### FASE 4 — AUTORIDADE EXTERNA (sinais off-site)
> Prazo: contínuo

#### 4.1 · Google Business Profile
Criar e otimizar perfil completo: nome exato "Viva Vendas", telefone, área de atuação (Niterói — Camboinhas, Icaraí, Ingá, Piratininga), fotos dos empreendimentos, descrição com keywords naturais. Responder todas as avaliações. **LLMs verificam GBP para confirmar existência de negócios locais.**

#### 4.2 · Perfis em Portais Imobiliários
Presença consistente no Zap Imóveis e VivaReal com NAP idêntico ao do site. Esses portais são frequentemente citados por IA — co-menção com Viva Vendas aumenta reconhecimento de entidade.

#### 4.3 · Instagram e YouTube como Fontes Secundárias
Conteúdo em vídeo sobre bairros e empreendimentos com descrições completas (título + texto longo). O YouTube é rastreado por Perplexity e Gemini como fonte de autoridade.

#### 4.4 · Wikidata / Wikipedia
Se possível, criar entrada no Wikidata para "Viva Vendas" e para "Conviva Engenharia" (construtora com R$2bi em VGV merece entrada). LLMs treinados em Wikipedia/Wikidata reconhecem entidades registradas com muito mais facilidade.

---

### FASE 5 — TÉCNICO AVANÇADO (diferencial competitivo)
> Prazo: paralelo

#### 5.1 · Melhorar Crawlabilidade

O site usa GSAP + JavaScript pesado. Verificar:
- Todo conteúdo essencial está no HTML estático (não renderizado só via JS)
- Evitar carregar texto importante via JS assíncrono
- `<noscript>` fallback para conteúdo crítico

#### 5.2 · Core Web Vitals
- LCP (Largest Contentful Paint): < 2,5s
- CLS (Cumulative Layout Shift): < 0,1
- INP (Interaction to Next Paint): < 200ms

Otimizações: imagens com `width`/`height` explícitos, `loading="lazy"` nas fotos de equipe (já feito), `font-display: swap`, pré-carregar fontes críticas.

#### 5.3 · robots.txt e Crawl Directives
Garantir que `robots.txt` não bloqueia crawlers de IA (Perplexity, OpenAI, Anthropic usam bots próprios):

```
User-agent: *
Allow: /
Sitemap: https://vivavendas.com.br/sitemap.xml

# Não bloquear bots de IA
User-agent: GPTBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Googlebot
Allow: /
```

#### 5.4 · hreflang (futuro)
Se o site vier a ter versão em inglês (para compradores estrangeiros), adicionar hreflang.

---

## PRIORIDADE DE EXECUÇÃO — CRONOGRAMA

| Semana | Ações |
|---|---|
| 1 | H1 em todas as 23 páginas + Open Graph básico |
| 2 | RealEstateAgent schema completo + Person schema (equipe) + BreadcrumbList |
| 3 | FAQPage schema em todas as páginas com FAQ + GeoCoordinates completo |
| 4 | HowTo schema (fgts.html, financiamento.html, calculadora.html) + Speakable |
| 5–6 | Apartment schema em imoveis/ + Article schema em páginas informacionais |
| 7–8 | Upgrade de conteúdo FAQ nas páginas de bairro (respostas longas) |
| 9–10 | Criar P1 e P2 (preço m² + comparativo Camboinhas vs Piratininga) |
| 11–12 | Criar P3, P4, P5 (retorno aluguel, Conviva histórico, financiamento) |
| 13–16 | Criar hub FAQ central + P6 e P7 |
| Contínuo | GBP, portais, YouTube, monitoramento com Perplexity/ChatGPT manual |

---

## MONITORAMENTO — COMO MEDIR SEM SEARCH CONSOLE

Enquanto o site não tiver histórico no Google Search Console, monitorar manualmente:

**Teste semanal — fazer as perguntas do Banco (3.1) diretamente para:**
- ChatGPT (gpt-4o)
- Perplexity
- Google com AI Overviews ativado
- Gemini

**Registrar:** se Viva Vendas é citada, qual concorrente é citado no lugar, quais fontes aparecem.

**Planilha de acompanhamento:**

| Query | Data | ChatGPT | Perplexity | Google AIO | Quem foi citado |
|---|---|---|---|---|---|
| "apartamento camboinhas niteroi" | Jun/26 | ✗ | ✗ | Zap Imóveis | Zap |
| "como usar fgts niteroi" | Jun/26 | ✗ | ✗ | CEF | CEF |

Meta: ao final de 6 meses, Viva Vendas deve aparecer em pelo menos 30% das queries do banco.

---

## CONCORRENTES A MONITORAR

| Tipo | Nome | Por quê monitorar |
|---|---|---|
| Portal nacional | Zap Imóveis | Maior autoridade de domínio, frequentemente citado |
| Portal nacional | VivaReal | Segunda maior autoridade |
| Construtora | Conviva Engenharia | Parceira — verificar se não compete |
| Imobiliária local | [pesquisar top Niterói] | Concorrente direto regional |
| Imobiliária local | [pesquisar top Niterói] | Concorrente direto regional |

**Como monitorar:** perguntar ao ChatGPT "quem são as melhores imobiliárias em Niterói para apartamentos à beira-mar?" — verificar quem aparece e analisar o site deles com a mesma auditoria deste documento.

---

## META FINAL — NOTA AEO ALVO

| Categoria | Atual | Meta 6 meses | Meta 12 meses |
|---|---|---|---|
| Schema geral | 8/10 | 10/10 | 10/10 |
| FAQPage schema | 4/10 | 9/10 | 10/10 |
| H1 semântico | 1/10 | 10/10 | 10/10 |
| Open Graph | 0/10 | 10/10 | 10/10 |
| HowTo schema | 0/10 | 7/10 | 10/10 |
| Speakable schema | 0/10 | 8/10 | 10/10 |
| Person/Author E-E-A-T | 0/10 | 7/10 | 9/10 |
| Conteúdo Q&A | 4/10 | 7/10 | 10/10 |
| Autoridade externa | 2/10 | 5/10 | 8/10 |
| **NOTA GERAL** | **5,5/10** | **8/10** | **9,5/10** |

---

## VANTAGEM COMPETITIVA — O QUE OS CONCORRENTES NÃO FAZEM

A maioria das imobiliárias regionais brasileiras:
- Não tem `Speakable` schema (zero no mercado local)
- Não tem `HowTo` schema
- Não tem `Person` schema para corretores
- Não tem H1 semântico em páginas de imóvel
- Não responde perguntas específicas de preço no HTML
- Usa plataformas genéricas (Facilita, CV CRM) com schema fraco

**Oportunidade:** Viva Vendas, por ser um site custom, pode implementar tudo isso sem limitações de plataforma. Isso é uma vantagem técnica real.

---

*Documento atualizado conforme implementações. Próxima revisão: Dezembro 2026.*
