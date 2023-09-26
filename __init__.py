from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import dotenv_values
from datetime import datetime, timedelta
import time

config = dotenv_values(".env")

number_of_tries = 10
sleep_time = 1
time_offset = int(config["TIME_OFFSET"])
include_weekends = str(config["WEEKENDS"])
booking_days_range = int(config["DAYS"])
office_id = str(config["OFFICE_ID"])


def sleep_with_offset(t: int):
    sleep_time = t + time_offset
    if sleep_time <= 0:
        return
    time.sleep(sleep_time)


def execute_until_successful(fn):
    for _ in range(number_of_tries):
        try:
            return fn()
        except Exception:
            sleep_with_offset(sleep_time)


def get_driver():
    match str(config["BROWSER"]).lower():
        case "chrome":
            driver = webdriver.Chrome()
        case "firefox":
            driver = webdriver.Firefox()
        case "safari":
            driver = webdriver.Safari()
        case _:
            driver = webdriver.Chrome()
    return driver


def book_desks():
    print(
        "----------------------------------------------------------------------------------------------------------\n"
        "THIS IS A VERY EARLY VERSION OF THE SCRIPT, IT MAY NOT WORK ON SOME MACHINES, READ THIS NOTE CAREFULLY!\n"
        "----------------------------------------------------------------------------------------------------------\n\n"
        "!!If the booking process fails, try to increase the TIME_OFFSET value in .env file!!\n\n"
        "It will not(!) check if you already booked a desk. It will sent booking"
        "request any way,\nso if you already booked a desk especially(!) in other wework(location) "
        "it then can cost you wework credits, so please be careful!\n\n"
        "If you have spotted some bug or if you have any suggestions, feel free to create issues on Github repo or contact me on vladimir@kavalerov.net.\n\n"
        f"{str(config['BROWSER'])} is starting.\n\n"
    )
    sleep_with_offset(5)
    driver = get_driver()
    driver.set_window_size(600, 800)
    driver.set_window_position(0, 0)

    # Login
    driver.get("https://members.wework.com")
    execute_until_successful(
        lambda: (
            driver.find_element(By.ID, "1-email").send_keys(config["EMAIL"]),
            driver.find_element(By.ID, "1-password").send_keys(config["PASSWORD"]),
            driver.find_element(By.ID, "1-submit").click(),
        )
    )
    sleep_with_offset(2)

    driver.get("https://members.wework.com/desks")
    sleep_with_offset(5)

    # Fetch today's date
    driver.find_element(
        By.XPATH,
        "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div",
    ).click()
    sleep_with_offset(2)
    today_date = datetime.strptime(
        driver.find_element(
            By.XPATH,
            "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div[3]",
        )
        .find_element(By.CSS_SELECTOR, "div[aria-selected='true']")
        .get_attribute("aria-label"),
        "%a %b %d %Y",
    )
    current_month = today_date.month

    # Book a table for today
    execute_until_successful(
        lambda: driver.find_element(
            By.XPATH, f"//*[@id='{office_id}']/section/button"
        ).click()
    )
    sleep_with_offset(2)
    execute_until_successful(
        lambda: driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/span[3]/button"
        ).click()
    )
    print(
        f"An attempt to make booking for {today_date.strftime('%a %b %d %Y')} has been made."
    )
    sleep_with_offset(2)

    for _ in range(today_date.day, today_date.day + booking_days_range):
        today_date: datetime = today_date + timedelta(days=1)

        # Skip weekends if WEEKENDS in .env is set to false
        if include_weekends.lower() == "false" and today_date.weekday() >= 5:
            continue

        driver.get("https://members.wework.com/desks")
        sleep_with_offset(5)

        # Open date selector
        execute_until_successful(
            lambda: driver.find_element(
                By.XPATH,
                "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div",
            ).click()
        )
        sleep_with_offset(0.5)

        # Check if we are still in the same month
        if today_date.month != current_month:
            execute_until_successful(
                lambda: driver.find_element(
                    By.XPATH,
                    "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[1]/span[2]",
                ).click()
            )
            sleep_with_offset(0.5)

        # Select next date in calendar
        execute_until_successful(
            lambda: driver.find_element(
                By.XPATH,
                "//*[@id='root']/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div[3]",
            )
            .find_element(
                By.CSS_SELECTOR,
                f"div[aria-label='{today_date.strftime('%a %b %d %Y')}']",
            )
            .click()
        )
        sleep_with_offset(1)

        # Book a table for today
        execute_until_successful(
            lambda: driver.find_element(
                By.XPATH, f"//*[@id='{office_id}']/section/button"
            ).click()
        )
        sleep_with_offset(2)
        execute_until_successful(
            lambda: driver.find_element(
                By.XPATH, "/html/body/div[2]/div/div[2]/span[3]/button"
            ).click()
        )
        print(
            f"An attempt to make booking for {today_date.strftime('%a %b %d %Y')} has been made."
        )
        sleep_with_offset(2)

    sleep_with_offset(3)
    print(
        "The booking process is finished, but there is no confirmation if the booking process went successfully.\n"
        f"Your request was to book a desk for {booking_days_range} day(s)",
        "including" if include_weekends.lower() == "true" else "without" " weekends.",
    )
    driver.close()


if __name__ == "__main__":
    book_desks()
