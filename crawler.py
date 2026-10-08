import asyncio
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright

async def crawl(start_url: str):
    timeout = 20
    visited = 0
    login_url = 'https://idp.transferegov.sistema.gov.br/idp/'
    usual_url = 'https://discricionarias.transferegov.sistema.gov.br/voluntarias/ConsultarNotasFiscais/ConsultarNotasFiscais.do?destino=ConsultarNotasFiscais&d-16544-t=notasFiscais&d-16544-p=2&d-16544-g=1'

    async with async_playwright() as p:
        print("Hi Crawler")
        browser = await p.firefox.launch()
        page = await browser.new_page()
        await page.goto(start_url)
        print(await page.title())
        await browser.close()