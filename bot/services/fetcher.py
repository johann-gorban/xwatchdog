from playwright.async_api import async_playwright
from typing import List
import logging
import re


playwright_instance = None
browser = None


async def init_fetcher():
    global playwright_instance, browser

    playwright_instance = await async_playwright().start()
    browser = await playwright_instance.firefox.launch()
    logging.info("Playwright initialized")


async def close_fetcher():
    global playwright_instance, browser
    if browser:
        await browser.close()
    if playwright_instance:
        await playwright_instance.stop()
    logging.info("Playwright closed")


async def fetch_width(url: str) -> float | None:
    global browser

    if not browser or not browser.is_connected():
        logging.warning("Browser is not available, reinitializing...")
        await init_fetcher()

    logging.info(f"Start fetching width from {url}")
    page = await browser.new_page()
    try:
        await page.goto(url)
        logging.info("Page loaded")
        await page.wait_for_selector(".h-\\[4px\\].rounded-full.relative.z-1")

        style_str: str = await page.eval_on_selector(
            ".h-\\[4px\\].rounded-full.relative.z-1",
            "el => el.getAttribute('style')"
        )
        logging.info(f"Full style attribute: {style_str}")
    except Exception as e:
        logging.error(f"Error fetching width: {e}")
        await page.close()
        return None

    await page.close()

    matches: List[str] = re.findall(r'(\d+(?:\.\d+)?)%', style_str)
    width: float = float(matches[-1].rstrip('%')) if matches else None

    logging.info(f'Get width: {width}')

    return width