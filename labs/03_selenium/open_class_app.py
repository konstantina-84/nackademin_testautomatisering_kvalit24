from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_navigate_to_signup():
    # Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    login_btn_signup = driver.find_element("id", "signup")

    # Act
    login_btn_signup.click()

    username_input_field = driver.find_element(
        "xpath", '//*[@id="root"]/div/div/input[1]'
    )

    time.sleep(10)  # wait 9 seconds.

    username_input_field.send_keys("admin_dev")

    password_input_field = driver.find_element(
        "xpath", '//*[@id="root"]/div/div/input[2]'
    )

    time.sleep(10)  # wait 9 seconds.

    password_input_field.send_keys("pass_1234")

    signup_btn = driver.find_element(By.CLASS_NAME, "button-primary")
    signup_btn.click()
    # Teardown
    driver.quit()
