from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

number_of_tries = 15
sleep_time = 0.5


def execute_until_successful(fn):
    for _ in range(number_of_tries):
        try:
            return fn()
        except Exception:
            print(_)
            time.sleep(sleep_time)


t = int(os.environ.get("TIME"))

driver = webdriver.Safari()
driver.get("https://members.wework.com")
execute_until_successful(
    lambda: (
        driver.find_element(By.ID, "1-email").send_keys(os.environ.get("EMAIL")),
        driver.find_element(By.ID, "1-password").send_keys(os.environ.get("PASSWORD")),
        driver.find_element(By.ID, "1-submit").click(),
    )
)
time.sleep(2)

driver.get("https://members.wework.com/desks")
time.sleep(6)

driver.find_element(
    By.XPATH,
    "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div",
).click()
time.sleep(2)

today_date = datetime.strptime(
    driver.find_element(
        By.XPATH,
        "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div[3]",
    )
    .find_element(By.CSS_SELECTOR, "div[aria-selected='true']")
    .get_attribute("aria-label"),
    "%a %b %d %Y",
)

for i in range(today_date.day, 31):
    today_date: datetime = today_date + timedelta(days=1)
    print(today_date.strftime("%a %b %d %Y"))
    execute_until_successful(
        lambda: driver.find_element(
            By.XPATH, f"//*[@id='{os.environ.get('OFFICE_ID')}']/section/button"
        ).click()
    )
    time.sleep(2)
    execute_until_successful(
        lambda: driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/span[3]/button"
        ).click()
    )
    time.sleep(2)
    driver.get("https://members.wework.com/desks")

    time.sleep(6)
    execute_until_successful(
        lambda:
    driver.find_element(
            By.XPATH,
            "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div",
        ).click()
    )
    
    execute_until_successful(
        lambda: driver.find_element(
            By.XPATH,
            "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div[3]",
        )
        .find_element(
            By.CSS_SELECTOR, f"div[aria-label='{today_date.strftime('%a %b %d %Y')}']"
        )
        .click()
    )

time.sleep(3)
driver.close()
