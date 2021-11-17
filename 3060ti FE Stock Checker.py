from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from twilio.rest import Client

import time

while True:
    # create a Twilio account to get account sid/auth token
    client = Client("ENTER ACCOUNT SID", "ENTER AUTH TOKEN")
    service = Service("C:\webdrivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # enter link of item to check
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")

    print(driver.title)
    el = driver.find_element(By.TAG_NAME, "body")
    str = el.text

    if (str.find("Sold Out") != -1):
        print("3060ti is still not available at Best Buy")
        driver.close()
        time.sleep(10) # program checks every 10 seconds if item is in stock
    else:
        # create a Twilio account and get a number through them (free)
        print("3060ti IS NOW AVAILABLE Best Buy")
        client.messages.create(to="+yourCellNumber", from_="+yourTwilioNumber", body="3060ti is now available!!! Go to: www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")
        driver.close()
        time.sleep(300) # program will resend text notification every 5 minutes if item is in stock
