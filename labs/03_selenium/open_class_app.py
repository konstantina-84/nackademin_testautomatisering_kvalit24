from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_signup_create_user():
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(APP_URL)
        time.sleep(2)

        login_btn_signup = driver.find_element("id", "signup")
        login_btn_signup.click()
        time.sleep(2)

        username_input = driver.find_element(
            "xpath", '//input[@placeholder="Username"]'
        )
        username_input.send_keys("admin_user")

        password_input = driver.find_element(
            "xpath", '//input[@placeholder="Password"]'
        )
        password_input.send_keys("pass_1234")

        time.sleep(1)

        signup_button = driver.find_element(
            "xpath", '//button[@class="button-primary" or normalize-space()="Sign Up"]'
        )
        signup_button.click()

        time.sleep(3)
    finally:
        driver.quit()
