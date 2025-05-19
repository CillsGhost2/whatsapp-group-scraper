
# Scrapper de Grupos do WhatsApp via Bing Search

Este projeto contém dois scripts Python que, utilizando a biblioteca **Playwright**, realizam:

1. **Busca automática de links de grupos do WhatsApp através do Bing**
2. **Verificação de quais grupos ainda estão ativos/funcionando**

As evidências são salvas em arquivos `.txt` e prints da tela são gerados automaticamente.

---

## Requisitos

- Python 3.8+
- [Playwright](https://playwright.dev/python/) com Chromium instalado
- `nest_asyncio`
- Conexão estável com a internet

Instalação dos requisitos:

```bash
pip install playwright nest_asyncio
playwright install
```

---

## Scripts

### 1. `buscar_grupos.py`

Busca links de grupos do WhatsApp com base em resultados do Bing.

#### Parâmetros (dentro do código):
- `output_file="whatsapp_groups.txt"`: arquivo onde os links serão salvos
- `limit=500`: número máximo de links a serem encontrados

#### Saídas:
- Arquivo `whatsapp_groups.txt` com os links encontrados
- Prints das páginas em `print_bing_{página}.png`

---

### 2. `verificar_grupos.py`

Verifica os links salvos e determina quais grupos ainda estão ativos.

#### Parâmetros (dentro do código):
- `input_file="whatsapp_groups.txt"`
- `output_file="whatsapp_groups_funcionando.txt"`

#### Saídas:
- Arquivo `whatsapp_groups_funcionando.txt` com os grupos ativos
- Prints das páginas de verificação em `printscreen_check_whatsapp_page_{id}.png`

---

## Exemplo de Saída

```
Encontrado: https://chat.whatsapp.com/Exemplo123
Print 'printscreen_bing_page_1.png'
...
Funcionando: https://chat.whatsapp.com/Exemplo123
Print 'Pagina_Grupo_Exemplo123.png'
```

---

## Observações

- Os scripts utilizam Playwright de forma assíncrona e controlada com `asyncio` e `nest_asyncio`.
- O algoritmo identifica grupos inválidos com base em imagens específicas da página de erro.
- Prints são úteis para auditoria e verificação manual dos resultados.

---
