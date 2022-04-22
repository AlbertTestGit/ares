from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import json

import helper

with open('settings.json', 'r', encoding='utf-8') as file:
    settings = json.loads(file.readline())


ua = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={ua.random}")
driver = webdriver.Chrome(
    executable_path='/home/amirzhan/Projects/hackathon/ares/drivers/chromedriver',
    options=options
)


def send_fake_data():
    driver.get(url=settings['url'])

    for inp in settings['ids']:
        elem = driver.find_element(By.NAME, inp['id'])

        if inp['type'] == 1:
            data = helper.random_name()
        elif inp['type'] == 2:
            data = helper.random_surname()
        elif inp['type'] == 3:
            pass
        elif inp['type'] == 4:
            data = helper.random_card_number()
        elif inp['type'] == 5:
            data = helper.random_expire_date()
        elif inp['type'] == 6:
            data = helper.random_cvv()
        elif inp['type'] == 7:
            data = helper.random_amount()
        elif inp['type'] == 8:
            data = helper.random_email()

        elem.send_keys(data)

    button = driver.find_element(By.NAME, 'submit')
    button.click()

try:
    while True:
        send_fake_data()
        time.sleep(5)
except:
    pass
finally:
    driver.close()
    driver.quit()


