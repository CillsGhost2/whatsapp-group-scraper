import asyncio
from playwright.async_api import async_playwright
import re
import time
import random
import nest_asyncio

async def check_whatsapp_group(page, link, outfile):
    try:
        await page.goto(link, wait_until="load", timeout=60000)
        await asyncio.sleep(random.randint(1,2))

        await capture_screenshot(page, link)

        content = await page.content()
        if "_0dVljceIA5.png" in content:
          print(f"Nao Funcionando: {link}")
          return "Não Funcionando"
        else:
            print(f"Funcionando: {link} ")
            outfile.write(f"{link}\n")
            outfile.flush()
            return "Funcionando"

    except Exception as e:
        print(f"Erro: {link} - {e}")
        return "Erro"

async def capture_screenshot(page, link):
  try:
     await page.screenshot(path=f"printscreen_check_whatsapp_page_{link.split('/')[-1]}.png")
     print(f"Print 'Pagina_Grupo_{link.split('/')[-1]}.png'")
  except Exception as e:
      print(f"Erro na print da página {link}: {e}")

async def main(input_file="whatsapp_groups.txt", output_file="whatsapp_groups_funcionando.txt"):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        with open(output_file, "a+") as outfile:
            with open(input_file, "r") as infile:
                for link in infile:
                    link = link.strip()
                    await check_whatsapp_group(page, link, outfile)
        await browser.close()

    print(f"Links salvos '{output_file}'")

async def main_wrapper():
  await main()

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.run(main_wrapper())