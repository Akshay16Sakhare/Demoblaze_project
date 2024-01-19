import time

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeServices
from selenium.webdriver.common.action_chains import ActionChains


url = "https://www.musicca.com/piano"
driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)
key_A = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/article[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[13]/span[1]/i[1]")
key_E = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/article[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[17]/span[1]/i[1]")
key_B= driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/article[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[14]/span[1]/i[1]")
key_C = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/article[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[15]/span[1]/i[1]")

#string A
key_A.click()
time.sleep(0.6)
key_E.click()
time.sleep(1)
key_A.click()
time.sleep(0.5)
key_E.click()
time.sleep(0.5)
key_A.click()

time.sleep(0.5)
#string A
key_B.click()
time.sleep(0.6)
key_E.click()
time.sleep(1)
key_B.click()
time.sleep(0.5)
key_E.click()
time.sleep(0.5)
key_B.click()

time.sleep(0.5)
#string A
key_C.click()
time.sleep(0.6)
key_E.click()
time.sleep(1)
key_C.click()
time.sleep(0.5)
key_E.click()
time.sleep(0.5)
key_C.click()

time.sleep(5)