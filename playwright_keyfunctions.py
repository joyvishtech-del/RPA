from playwright.async_api import async_playwright
import asyncio
async def playwright_function():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.google.com')
        await page.wait_for_timeout(5000)  # Wait for 5 seconds
        await page.fill('input[name="q"]', 'Playwright Python')
        await page.press('input[name="q"]', 'Enter')
        await page.wait_for_selector('h3')  # Wait for search results to load
        print("Search completed successfully.")
        await browser.close()   
if __name__ == "__main__":
    import asyncio
    asyncio.run(playwright_function())