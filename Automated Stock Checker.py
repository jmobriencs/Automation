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
    driver.get("URL GOES HERE")

    print(driver.title)
    el = driver.find_element(By.TAG_NAME, "body")
    str = el.text
    
    #  Modify the text in the str.find if "Sold Out" doesn't appear on the page (i.e. Not Available, Not In Stock, etc)
    if (str.find("Sold Out") != -1):
        print("ITEM NAME HERE is still not available.")
        driver.close()
        time.sleep(10) # program checks every 10 seconds if item is in stock
    else:
        # create a Twilio account and get a number through them (free)
        print("ITEM NAME HERE is now available!!!")
        client.messages.create(to="+yourCellNumber", from_="+yourTwilioNumber", body="ITEM NAME HERE is now available!!! Go to: INSERT URL HERE")
        driver.close()
        time.sleep(300) # program will resend text notification every 5 minutes if item is in stock
