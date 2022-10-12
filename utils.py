from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import rand_str


def wait_and_click(driver: WebDriver, by: str, search_str: str):
    element = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((by, search_str))
    )
    browser_click(driver, element)


def click_in_list_by_text(
    driver: WebDriver, by: str, search_str: str, element_text: str
):
    elements = driver.find_elements(by, search_str)

    for element in elements:
        if element.text == element_text:
            browser_click(driver, element)


def browser_click(driver, element: WebElement):
    driver.execute_script("arguments[0].click();", element)


def read_file(name):
    file = open(name, "r")
    content = file.read()
    return content.split("\n")[:-1]
