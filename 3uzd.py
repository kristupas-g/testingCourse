from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import rand_str
import utils

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 40)

driver.get("https://demowebshop.tricentis.com/")

driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]').click()

utils.click_in_list_by_text(driver, By.TAG_NAME, "span", "Web Tables")


while driver.find_element(By.CLASS_NAME, "-totalPages").text != "2":
    utils.wait_and_click(driver, By.ID, "addNewRecordButton")

    form_fields = driver.find_element(By.ID, "userForm").find_elements(
        By.TAG_NAME, "input"
    )

    for field in form_fields:
        field_id = field.get_attribute("id")
        if field_id == "userEmail":
            field.send_keys("a@gmail.com")
        elif field_id == "age" or field_id == "salary":
            field.send_keys("1")
        else:
            field.send_keys("a")

    driver.find_element(By.ID, "submit").click()

next_button = driver.find_element(By.CLASS_NAME, "-next").find_element(
    By.TAG_NAME, "button"
)

utils.browser_click(driver, next_button)

action_buttons = driver.find_element(By.CLASS_NAME, "action-buttons").find_elements(
    By.TAG_NAME, "span"
)

for button in action_buttons:
    if button.get_attribute("title") == "Delete":
        utils.browser_click(driver, button)
        break


assert driver.find_element(By.CLASS_NAME, "-totalPages").text == "1"

driver.close()
