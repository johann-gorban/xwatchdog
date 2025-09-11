from playwright.async_api import async_playwright
import asyncio
import logging


async def fetch_width(url: str) -> float | None:
    logging.info(f"Start fetching width from {url}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        logging.info("Page loaded")

        await asyncio.sleep(5)
        logging.info("Waited 5 seconds for dynamic content")

        try:
            await page.wait_for_selector(".h-\\[4px\\].rounded-full.relative.z-1", timeout=15000)
            width: str = await page.eval_on_selector(
                ".h-\\[4px\\].rounded-full.relative.z-1",
                "el => el.style.width"
            )
            logging.info(f"Raw width from style: '{width}'")
        except Exception as e:
            logging.error(f"Error fetching width: {e}")
            await browser.close()
            return None

        await browser.close()

        if width and width.endswith('%'):
            value = float(width.rstrip('%'))
            logging.info(f"Parsed width: {value}%")
            return value
        else:
            logging.warning("Width is empty or not in percent format")
            return None

