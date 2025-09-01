from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_admin_add_product():
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    # === LOGIN AS ADMIN ===
    login_btn = driver.find_element(By.CLASS_NAME, "button_primary")
    login_btn.click()

    time.sleep(1)  # vänta in formuläret

    username_input = driver.find_element("id", "username")
    password_input = driver.find_element("id", "password")
    submit_btn = driver.find_element("id", "login-submit")

    username_input.send_keys("admin")
    password_input.send_keys("adminpassword")
    submit_btn.click()

    time.sleep(2)  # vänta på navigation

    # === NAVIGATE TO ADD PRODUCT PAGE ===
    add_product_btn = driver.find_element("id", "add-product")
    add_product_btn.click()

    time.sleep(1)

    # === FILL IN PRODUCT FORM ===
    product_name = driver.find_element("id", "product-name")
    product_price = driver.find_element("id", "product-price")
    product_desc = driver.find_element("id", "product-description")
    submit_product_btn = driver.find_element("id", "submit-product")

    product_name.send_keys("Testprodukt")
    product_price.send_keys("199")
    product_desc.send_keys("Detta är en testprodukt som skapats via Selenium.")

    submit_product_btn.click()

    time.sleep(3)

    product_list = driver.find_element("id", "product-list")
    assert "Testprodukt" in product_list.text

    driver.quit()
