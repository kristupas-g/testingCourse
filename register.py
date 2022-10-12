from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import rand_str
import utils
import pytest


@pytest.fixture
def register():
    driver = webdriver.Chrome()

    driver.get("https://demowebshop.tricentis.com/")

    driver.find_element(By.CLASS_NAME, "ico-register").click()

    form_fields = driver.find_elements(By.CLASS_NAME, "form-fields")
    driver.find_element(By.ID, "gender-male").click()

    email = rand_str.get_random_email()
    password = rand_str.get_random_string(12)

    for form_field in form_fields:
        input_fields = form_field.find_elements(By.TAG_NAME, "input")
        for field in input_fields:
            if field.accessible_name == "Email:":
                field.send_keys(email)
            elif field.get_property("type") == "password":
                field.send_keys(password)
            else:
                field.send_keys(rand_str.get_random_string(12))

    driver.find_element(By.XPATH, '//*[@id="register-button"]').click()

    driver.close()

    return (email, password)
