from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

class Demo_Blaze_ele():

    sign_up_opt_selector = (By.ID, "signin2")
    userName_selector = (By.ID, "sign-username")
    passWord_selector = (By.ID, "sign-password")
    submit_button_selector = (By.XPATH, "//div/button[contains(text(), 'Sign up')]")

    login_opt_selector = (By.ID, "login2")
    login_username_selector = (By.ID, "loginusername")
    login_password_selector = (By.ID, "loginpassword")
    login_button_selector = (By.XPATH, "//button[contains(text(),'Log in')]")
    logout_selector = (By.XPATH, "//a[@id='logout2']")

    product_1_selector = (By.LINK_TEXT, "Iphone 6 32gb")
    product_2_selector = (By.LINK_TEXT, "Sony xperia z5")
    addtoCart_selector = (By.XPATH, "//a[contains(text(), 'Add to cart')]")
    gotoCart_selector = (By.XPATH, "//a[contains(text(), 'Cart')]")
    home_selector = (By.XPATH, "//li[@class='nav-item active']//a[@class='nav-link']")
    total_selector = (By.XPATH, "//h3[@id='totalp']")
    place_order_selector = (By.XPATH, "//button[normalize-space()='Place Order']")

    order_name_ele = (By.XPATH, "//input[@id='name']")
    order_country_ele = (By.XPATH,"//input[@id='country']")
    order_city_ele = (By.XPATH,"//input[@id='city']")
    order_card_ele = (By.XPATH,"//input[@id='card']")
    order_month_ele = (By.XPATH,"//input[@id='month']")
    order_year_ele = (By.XPATH,"//input[@id='year']")
    order_purchase_ele = (By.XPATH,"//button[contains(text(),'Purchase')]")





    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def sign_up_option(self):
        self.wait.until(EC.presence_of_element_located((self.sign_up_opt_selector))).click()

    def enter_userName(self, Name):
        self.wait.until(EC.presence_of_element_located((self.userName_selector))).send_keys(Name)

    def enter_passWord(self, Password):
        self.wait.until(EC.presence_of_element_located((self.passWord_selector))).send_keys(Password)

    def click_submit_button(self):
        self.wait.until(EC.presence_of_element_located((self.submit_button_selector))).click()

    def click_login_opt(self):
        self.wait.until(EC.presence_of_element_located((self.login_opt_selector))).click()

    def enter_login_userName(self, Name):
        self.wait.until(EC.presence_of_element_located((self.login_username_selector))).send_keys(Name)

    def enter_login_passWord(self, Password):
        self.wait.until(EC.presence_of_element_located((self.login_password_selector))).send_keys(Password)

    def click_login_button(self):
        self.wait.until(EC.presence_of_element_located((self.login_button_selector))).click()

    def click_logout_button(self):
        self.wait.until(EC.presence_of_element_located((self.logout_selector))).click()

    def click_prod_1(self):
        self.wait.until(EC.presence_of_element_located((self.product_1_selector))).click()

    def click_prod_2(self):
        self.wait.until(EC.presence_of_element_located((self.product_2_selector))).click()

    def add_products(self):
        self.wait.until(EC.presence_of_element_located((self.addtoCart_selector))).click()
        # self.driver.switch_to(self.alert).accept()

    def go_to_cart(self):
        self.wait.until(EC.presence_of_element_located((self.gotoCart_selector))).click()

    def click_home_button(self):
        self.wait.until(EC.presence_of_element_located((self.home_selector))).click()

    def click_place_order(self):
        self.wait.until(EC.presence_of_element_located((self.place_order_selector))).click()

    def Place_order_Name(self, Name):
        self.wait.until(EC.presence_of_element_located((self.order_name_ele))).send_keys(Name)

    def Place_order_Country(self, Country):
        self.wait.until(EC.presence_of_element_located((self.order_country_ele))).send_keys(Country)

    def Place_order_City(self, City):
        self.wait.until(EC.presence_of_element_located((self.order_city_ele))).send_keys(City)

    def Place_order_Creditcard(self, Number):
        self.wait.until(EC.presence_of_element_located((self.order_card_ele))).send_keys(Number)

    def Place_order_Month(self, Month):
        self.wait.until(EC.presence_of_element_located((self.order_month_ele))).send_keys(Month)

    def Place_order_Year(self, Year):
        self.wait.until(EC.presence_of_element_located((self.order_year_ele))).send_keys(Year)

    def click_purchase_button(self):
        # self.wait.until(EC.element_to_be_clickable((self.order_purchase_ele))).click()
        self.driver.execute_script("arguments[0].click();", self.wait.until(EC.element_to_be_clickable((self.order_purchase_ele))))




