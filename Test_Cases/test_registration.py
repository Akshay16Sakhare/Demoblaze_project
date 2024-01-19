import time
from Test_Cases.conftest import setup
from POM_Demo_blaze.DemoBlaze_POM import Demo_Blaze_ele
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Test_registration():

    def test_registration(self, setup):

        self.driver = setup
        self.regi = Demo_Blaze_ele(self.driver)
        self.driver.implicitly_wait(5)
        self.regi.sign_up_option()
        self.regi.enter_userName("akshay16")
        self.regi.enter_passWord("testing@123")
        self.regi.click_submit_button()

        # self.driver.save_screenshot(r"C:\Users\Admin\PycharmProjects\Demo_Blaze_New\screenshots\SS.jpg")

        time.sleep(5)
        self.driver.close()

