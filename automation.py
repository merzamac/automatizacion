from playwright.sync_api import sync_playwright
import os

NUMBER = "00000000"  # colocar el numero
USER_DATA_DIR = "./whatsapp_session"
WHATSAPP = "https://web.whatsapp.com/"
CHAT_URL = f"https://web.whatsapp.com/send?phone={NUMBER}"
MESSAGE = "Prueba Realizada"  # el mensje va aqui


def automated_sending(MESSAGE, NUMBER):
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            channel="chrome",
            headless=False,
            slow_mo=1000,
        )
        page = browser.new_page()
        page.goto(WHATSAPP)
        page.wait_for_selector('div[id="side"]', timeout=30000)
        page.goto(CHAT_URL)
        page.locator('//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').fill(MESSAGE)
        page.get_by_role("button").and_(page.get_by_label("Send")).click()
        page.wait_for_selector('span[aria-label=" Read "]', timeout=30000)
        #page.wait_for_timeout(9999000)
        browser.close()


if __name__ == "__main__":
    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)

    automated_sending(MESSAGE, NUMBER)
