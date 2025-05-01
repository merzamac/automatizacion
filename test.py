from playwright.sync_api import sync_playwright


def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            slow_mo=1000,
        )
        # raise ValueError
        page = browser.new_page()
        page.goto("https://playwright.dev/python/")

        #element = page.locator("#__docusaurus_skipToContent_fallback > .hero > .container > .buttons_pzbO > a:has-text('Get started')").text_content()
        page.locator("#__docusaurus_skipToContent_fallback > .hero > .container > .buttons_pzbO > a").click()
        # page.locator("#main > footer > lexical-rich-text-input > p :has-text('Type a message')").click()
        #lexical-rich-text-input
        #print(element)

        # page.wait_for_selector('span[aria-hidden="True"]', timeout=60000)
        # time.sleep(5)
        page.wait_for_timeout(5000)
        browser.close()
        # footer .copyable-area .x1n2onr6 span ._ak1q ._ak1r .x9f619 .lexical-rich-text-input

if __name__ == "__main__":
    test()
