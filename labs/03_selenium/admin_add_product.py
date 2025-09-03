from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_login_and_add_product():
    driver = webdriver.Chrome(options=options)

    try:
        # --- LOGIN ---
        driver.get(APP_URL)
        time.sleep(5)

        username_input = driver.find_element(
            "xpath", '//input[@placeholder="Username"]'
        )
        username_input.send_keys("admin_user")

        password_input = driver.find_element(
            "xpath", '//input[@placeholder="Password"]'
        )
        password_input.send_keys("pass_1234")

        time.sleep(2)
        login_button = driver.find_element("xpath", '//button[@class="button-primary"]')
        login_button.click()

        # --- ADD PRODUCT ---
        time.sleep(5)

        product_name_input = driver.find_element(
            "xpath", '//input[@placeholder="Product Name"]'
        )
        product_name_input.send_keys("peach")

        create_product_button = driver.find_element(
            "xpath", '//button[contains(text(),"Create Product")]'
        )
        create_product_button.click()

        time.sleep(3)

        added_product = driver.find_element("xpath", '//span[contains(text(),"peach")]')
        #    assert "peach" in added_product.text
        assert added_product.text.strip() == "peach"

    finally:
        driver.quit()
