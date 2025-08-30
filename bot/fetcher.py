from playwright.async_api import async_playwright

async def fetch_width(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_selector(".h-\\[4px\\].rounded-full.relative.z-1", timeout=10000)
        width = await page.eval_on_selector(
            ".h-\\[4px\\].rounded-full.relative.z-1",
            "el => el.style.width"
        )
        await browser.close()
        return width

