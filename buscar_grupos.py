import asyncio
from playwright.async_api import async_playwright
import re
import time
import random
import nest_asyncio

async def get_whatsapp_links(page, limit, outfile, pagina):

    links_encontrados = []
    resultados_por_pagina = 10

    url_busca = f'https://www.bing.com/search?q=site:"chat.whatsapp.com"&first={(pagina - 1) * resultados_por_pagina + 1}'
    try:
        await page.goto(url_busca, wait_until="load")
        await page.wait_for_selector("li.b_algo", state="visible", timeout=60000)
    except Exception as e:
        print(f"Erro ao acessar a URL ou esperar os seletores: {e}")
        return links_encontrados

    resultados = await page.query_selector_all('li.b_algo')

    if not resultados:
        print(f"Nada na pág {pagina}.")
        return links_encontrados

    for result in resultados:
       try:
         link_tag = await result.query_selector('a[href]')
         if link_tag:
            href = await link_tag.get_attribute('href')
            if 'chat.whatsapp.com' in href:
               if href not in links_encontrados and len(links_encontrados) < limit:
                    links_encontrados.append(href)
                    print(f"Encontrado: {href} ")
                    if outfile:
                        outfile.write(href + "\n")
                        outfile.flush()
       except Exception as e:
           print(f"Erro ao extrair links: {e}")

    return links_encontrados

async def capture_screenshot(page, pagina):
  try:
     await page.screenshot(path=f"print_bing_{pagina}.png")
     print(f"Print 'printscreen_bing_page_{pagina}.png'")
  except Exception as e:
      print(f"Erro ao fazer o printscreen da página {pagina}: {e}")

async def main(output_file="whatsapp_groups.txt", limit=500):
    links_encontrados = []
    pagina = 1

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        with open(output_file, "a+") as outfile:
            while len(links_encontrados) < limit:
                novos_links = await get_whatsapp_links(page, limit, outfile, pagina)
                links_encontrados.extend(novos_links)

                if len(novos_links) == 0 :
                     print(f"Nada {pagina}. proxima")
                     break

                await capture_screenshot(page, pagina)
                print(f"shh, total: ({len(links_encontrados)}/{limit})")
                await asyncio.sleep(5)
                pagina+=1
        await browser.close()

    print(f"Links salvos '{output_file}'")

async def main_wrapper():
  await main()

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.run(main_wrapper())