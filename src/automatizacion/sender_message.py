from playwright.sync_api import sync_playwright,BrowserContext
import os
from .constants import *
from .helpers import which_comand
import pandas as pd

class Sender():
    @classmethod
    def whatsapp(self,message, numbers):
        if not os.path.exists(data_whatsapp):
            os.makedirs(data_whatsapp)
            
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=data_whatsapp,
                channel="chrome",
                headless=False,
                slow_mo=1000,
            )
            page = browser.new_page()
            page.goto(whatsapp_url)
            for number in numbers:
                page.wait_for_selector('nav[id="side"]')
                page.goto(chatw_url+number)
                page.locator('//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').fill(message)
                page.get_by_role("button").and_(page.get_by_label("Send")).click()
                page.wait_for_selector('span[aria-label=" Read "]')
                page.wait_for_timeout(5)
            browser.close()

    @classmethod
    def google(self,csv_path:str):
        if not os.path.exists(data_google):
            os.makedirs(data_google)
            
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=data_google,
                channel="msedge",
                headless=False,
                slow_mo=1000,
            )
        
            page = browser.new_page()
            page.goto(google_url)
            
            switch_save = page.get_by_role("switch" )
            
            if switch_save.count() > 0:
                switch_save.click()
                
            try:
                df = pd.read_csv(csv_path, delimiter=";")   
                for index, row in df.iterrows():
                    gps = row['fabricante']
                    phone_nomber = row['numero_chip']
                    
                    if gps in allgps:
                        comand = which_comand(gps)
                        if len(phone_nomber)  < 5:
                            continue
                        _execute(page,comand,phone_nomber)
            except Exception as e:
                print(f"Algo falló: {e}")
                return None
            
            
            # ---------------------
            #browser.close()
            
             
def _execute(page : BrowserContext,comand,phone_nomber):
    page.wait_for_selector('nav')
    page.locator('a[mat-button]').click()
    page.locator('input[class="input"]').fill(phone_nomber)
    page.locator('mw-contact-selector-button[class="ng-star-inserted"]').click()
    page.wait_for_timeout(5)
    page.wait_for_selector('textarea')
    page.locator('textarea[class="input"]').fill(comand)
    #page.locator('mws-message-send-button[class="inline-send-button"]').click()
    page.get_by_role("button", name="SMS").click()
    page.wait_for_timeout(5)