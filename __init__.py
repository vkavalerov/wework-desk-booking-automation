from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from dotenv import dotenv_values
from datetime import datetime, timedelta

config = dotenv_values(".env")

number_of_tries = 15
sleep_time = 0.5
time_offset = int(config["TIME_OFFSET"])


def sl(t):
    time.sleep(t + time_offset)


def execute_until_successful(fn):
    for _ in range(number_of_tries):
        try:
            return fn()
        except Exception:
            print(_)
            sl(sleep_time)


idays = int(config["DAYS"])
iweekends = str(config["WEEKENDS"])

driver = webdriver.Safari()
driver.get("https://members.wework.com")
execute_until_successful(
    lambda: (
        driver.find_element(By.ID, "1-email").send_keys(config["EMAIL"]),
        driver.find_element(By.ID, "1-password").send_keys(config["PASSWORD"]),
        driver.find_element(By.ID, "1-submit").click(),
    )
)
sl(2)

driver.get("https://members.wework.com/desks")
sl(6)

driver.find_element(
    By.XPATH,
    "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div",
).click()
sl(2)

today_date = datetime.strptime(
    driver.find_element(
        By.XPATH,
        "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div[3]",
    )
    .find_element(By.CSS_SELECTOR, "div[aria-selected='true']")
    .get_attribute("aria-label"),
    "%a %b %d %Y",
)

execute_until_successful(
    lambda: driver.find_element(
        By.XPATH, f"//*[@id='{config['OFFICE_ID']}']/section/button"
    ).click()
)

sl(2)
execute_until_successful(
    lambda: driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div[2]/span[3]/button"
    ).click()
)
print(f"A desk for {today_date.strftime('%a %b %d %Y')} successfully booked.")
sl(2)

for i in range(today_date.day, today_date.day + idays):
    today_date: datetime = today_date + timedelta(days=1)
    if iweekends.lower() == "false" and today_date.weekday() >= 5:
        continue

    driver.get("https://members.wework.com/desks")
    sl(6)

    execute_until_successful(
        lambda: driver.find_element(
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

    execute_until_successful(
        lambda: driver.find_element(
            By.XPATH, f"//*[@id='{config['OFFICE_ID']}']/section/button"
        ).click()
    )
    sl(2)

    execute_until_successful(
        lambda: driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/span[3]/button"
        ).click()
    )
    print(f"A desk for {today_date.strftime('%a %b %d %Y')} successfully booked.")
    sl(2)

sl(3)
print(
    f"You have successfully booked a desk for the next {idays} day(s)",
    "with" if iweekends.lower() == "true" else "without" " weekends.",
)
driver.close()
