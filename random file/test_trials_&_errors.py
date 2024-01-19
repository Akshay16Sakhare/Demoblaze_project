import time
from POM_Demo_blaze.DemoBlaze_POM import Demo_Blaze_ele
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeServices


url = "https://www.demoblaze.com/"
driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()

sign_up_opt_selector = (By.ID, "signin2")
userName_selector = (By.ID, "sign-username")
passWord_selector = (By.ID, "sign-password")
submit_button_selector = (By.XPATH, "//div/button[contains(text(), 'Sign up')]")

driver.find_element(By.ID, "signin2").click()
time.sleep(5)
driver.find_element(By.ID, "sign-username").send_keys("Akshay_")
driver.find_element(By.ID, "sign-password").send_keys("test@123")
driver.find_element(By.XPATH, "//div/button[contains(text(), 'Sign up')]").click()



time.sleep(5)
self.driver.close()





