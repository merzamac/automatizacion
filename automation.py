from playwright.sync_api import sync_playwright
import time

def automated_sending(mensaje, phone):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            slow_mo=1000,
        )
        page = browser.new_page()
        page.goto("https://web.whatsapp.com/")
        time.sleep(30)
        chat_url = f"https://web.whatsapp.com/send?phone={phone}"
        page.goto(chat_url)
        page.get_by_role("textbox", name="Type a message").get_by_role("paragraph").click()
        page.get_by_role("textbox", name="Type a message").fill(mensaje)
        page.get_by_role("button", name="Send").click()


        time.sleep(5)
        browser.close()

if __name__ == "__main__":
    mensaje = "Lo he conseguido tio"
    phone = '000000000000'
    automated_sending(mensaje, phone)
