import time
from selenium.webdriver.common.alert import Alert
from Test_Cases.conftest import setup
from POM_Demo_blaze.DemoBlaze_POM import Demo_Blaze_ele
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Test_cart():

    @property
    def wait(self):
        return WebDriverWait(self.driver, 10)

    def test_add_products(self, setup):
        self.driver = setup
        self.login = Demo_Blaze_ele(self.driver)
        self.driver.implicitly_wait(5)
        self.login.click_login_opt()
        self.login.enter_login_userName("akshay16")
        self.login.enter_login_passWord("testing@123")
        self.login.click_login_button()
        time.sleep(3)
        my_products = [self.login.product_1_selector, self.login.product_2_selector]

        for item in my_products:
            self.wait.until(EC.presence_of_element_located(item)).click()
            self.login.add_products()
            time.sleep(2)
            self.driver.switch_to.alert.accept()
            time.sleep(2)
            self.login.click_home_button()

        self.login.go_to_cart()
        print("Products added to cart.")

        time.sleep(2)
        total = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h3[@id='totalp']"))).text
        print("Your Total Amount To Pay : "+'$'+total)

        time.sleep(5)
        self.driver.close()

