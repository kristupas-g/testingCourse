import pytest
from register import register
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import utils
import rand_str


def test_digital_downloads(register):
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 40)

    driver.get("https://demowebshop.tricentis.com/")

    driver.find_element(By.CLASS_NAME, "ico-login").click()

    # Login logic
    driver.find_element(By.CLASS_NAME, "email").send_keys(register[0])
    driver.find_element(By.CLASS_NAME, "password").send_keys(register[1])
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input",
    ).click()

    driver.find_element(
        By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ul/li[5]/a"
    ).click()

    titles_to_add = utils.read_file(
        "/Users/kristupasgaidys/Documents/repos/testingCourse/data1.txt"
    )

    items = driver.find_elements(By.CLASS_NAME, "details")

    for title_to_add in titles_to_add:
        for item in items:
            item_title = item.find_element(By.CLASS_NAME, "product-title").text
            if item_title == title_to_add:
                item.find_element(By.TAG_NAME, "input").click()
                time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="topcartlink"]/a').click()
    driver.find_element(By.XPATH, '//*[@id="termsofservice"]').click()
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

    inputs = driver.find_element(By.CLASS_NAME, "edit-address").find_elements(
        By.TAG_NAME, "input"
    )

    for input in inputs:
        input.send_keys(rand_str.get_random_string(12))

    Select(driver.find_element(By.ID, "BillingNewAddress_CountryId")).select_by_index(1)

    driver.find_element(By.XPATH, '//*[@id="billing-buttons-container"]/input').click()

    utils.wait_and_click(
        driver, By.XPATH, '//*[@id="payment-method-buttons-container"]/input'
    )

    utils.wait_and_click(
        driver, By.XPATH, '//*[@id="payment-info-buttons-container"]/input'
    )

    utils.wait_and_click(
        driver, By.XPATH, '//*[@id="confirm-order-buttons-container"]/input'
    )

    driver.close()
