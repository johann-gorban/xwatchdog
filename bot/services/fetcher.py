from playwright.async_api import async_playwright
import asyncio


async def fetch_width(url: str) -> float:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)

        await asyncio.sleep(5)

        await page.wait_for_selector(".h-\\[4px\\].rounded-full.relative.z-1")
        width: str = await page.eval_on_selector(
            ".h-\\[4px\\].rounded-full.relative.z-1",
            "el => el.style.width"
        )

        await browser.close()

        if width:
            width = width.rstrip('%')
            width = float(width)

        return width

