import asyncio
from playwright.async_api import async_playwright

QUERY = "AI summit india"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Open Bing
        await page.goto("https://www.bing.com", wait_until="domcontentloaded")

        # Wait for the Bing search box
        box = page.locator("#sb_form_q")
        await box.wait_for(state="visible", timeout=30000)

        # Type query + search
        await box.click()
        await box.fill("")
        await page.type("#sb_form_q", QUERY, delay=50)
        await page.keyboard.press("Enter")

        # Wait for results
        first = page.locator("li.b_algo h2 a").first
        await first.wait_for(state="visible", timeout=30000)

        # ✅ Click first result AND wait for navigation
        async with page.expect_navigation(wait_until="domcontentloaded", timeout=60000):
            await first.click()

        # ✅ Wait until the target site finishes loading
        await page.wait_for_load_state("load")        # page load event
        await page.wait_for_load_state("networkidle") # mostly done with requests

        # Optional: wait for some real content (helps confirm page rendered)
        await page.wait_for_selector("body", timeout=30000)

        print("AI Summit website loaded:", page.url)

        # ✅ Keep browser open so you can see it (press Enter in terminal to close)
        input("Press Enter to close the browser...")

        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())