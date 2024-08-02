# Pages/Login_Page.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Qprime_Locators

locators = Qprime_Locators.Login_Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_username(self, username):
        username_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.User_Name_Field)))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.Password_Field)))
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Login_Button)))
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(8)
