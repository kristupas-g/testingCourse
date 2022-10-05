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

driver.get("https://demoqa.com/")

utils.wait_and_click(driver, By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]')

utils.click_in_list_by_text(driver, By.TAG_NAME, "span", "Progress Bar")

utils.wait_and_click(driver, By.ID, "startStopButton")

reset_button = wait.until(EC.presence_of_element_located((By.ID, "resetButton")))

reset_button.click()

progress_bar = driver.find_element(By.ID, "progressBar").find_element(
    By.TAG_NAME, "div"
)

utils.browser_click(driver, progress_bar)

assert progress_bar.text == ""

driver.close()
