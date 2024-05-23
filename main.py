from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from ad_register import ads
from ad_register import equip_intro
from ad_register import desc_outro

for ad in ads:
    print(ad)

driver_path = r"C:\Users\ve1t\Downloads\chromedriver-win64\chromedriver-win64\chromedriver"
url = 'https://www.kleinanzeigen.de/p-anzeige-aufgeben-schritt2.html'

# adding user profile
chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\Users\ve1t\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument(r"--profile-directory=Profile 2")  # Use your specific profile name here

# Initializing the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open 10 tabs and navigate to the website
for ad in ads:
    driver.execute_script(f"window.open('{url}', '_blank');")

# leave some time for loading
time.sleep(3)

i = 0
for ad in ads:
    # switch windo
    driver.switch_to.window(driver.window_handles[i+1])

    # add title
    field_element = driver.find_element(By.ID, "postad-title")
    field_element.send_keys(ad.title)

    # add price
    field_element = driver.find_element(By.ID, "micro-frontend-price")
    field_element.send_keys(int(ad.price))

    # add description
    field_element = driver.find_element(By.ID, "pstad-descrptn")
    description_str = ad.description
    description_str += equip_intro
    for entry in ad.equipment:
        description_str += entry.__str__()
    description_str += desc_outro
    field_element.send_keys(description_str)

    i += 1

input("Press Enter to close the browser...")
driver.quit()
