from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import rand_str

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/")

driver.find_element(
    By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a"
).click()

driver.find_element(
    By.XPATH,
    "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[3]/input",
).click()

form_fields = driver.find_elements(By.CLASS_NAME, "form-fields")
driver.find_element(By.ID, "gender-male").click()

for form_field in form_fields:
    input_fields = form_field.find_elements(By.TAG_NAME, "input")
    password = rand_str.get_random_string(12)
    for field in input_fields:
        if field.accessible_name == "Email:":
            field.send_keys(rand_str.get_random_email())
        elif field.get_property("type") == "password":
            field.send_keys(password)
        else:
            field.send_keys(rand_str.get_random_string(12))


driver.find_element(By.XPATH, '//*[@id="register-button"]').click()

driver.find_element(
    By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[2]/input"
).click()

driver.find_element(
    By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ul/li[2]/a"
).click()

driver.find_element(
    By.XPATH,
    "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/a/img",
).click()

items = driver.find_elements(By.CLASS_NAME, "details")

for item in items:
    price = item.find_element(By.CLASS_NAME, "prices")
    if float(price.text) >= 1500:
        item.find_element(By.TAG_NAME, "input").click()
        break

inputs = driver.find_elements(By.TAG_NAME, "input")

for input in inputs:
    if input.get_property("type") == "button":
        print(input.text)

time.sleep(10000)

driver.close()
