from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeServices


@pytest.fixture()
def setup():
    URL = "https://www.demoblaze.com/"
    # chrome_option = Options()
    # chrome_option.add_experimental_option("detach", True)
    # chrome_option.add_argument("headless")
    driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install())) #options=chrome_option
    driver.get(URL)
    driver.maximize_window()
    return driver



