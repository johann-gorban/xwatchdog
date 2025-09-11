from playwright.async_api import async_playwright
import logging


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
    logging.info(f"Start fetching width from {url}")
    page = await browser.new_page()
    try:
        await page.goto(url)
        logging.info("Page loaded")
        await page.wait_for_selector(".h-\\[4px\\].rounded-full.relative.z-1")

        width: str = await page.eval_on_selector(
            ".h-\\[4px\\].rounded-full.relative.z-1",
            "el => el.style.width"
        )
        logging.info(f"Raw width from style: '{width}'")
    except Exception as e:
        logging.error(f"Error fetching width: {e}")
        await page.close()
        return None

    await page.close()

    if width and width.endswith('%'):
        value = float(width.rstrip('%'))
        logging.info(f"Parsed width: {value}%")
        return value
    else:
        logging.warning("Width is empty or not in percent format")
        return None
