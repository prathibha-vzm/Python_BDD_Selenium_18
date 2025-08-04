# Importing needed packages
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Task_18.pages.base_page import BasePage # Importing Base page to use as parent class

# This page is for locating login page elements to enter text or to click on that element
# Locators are retrieved from a JSON file by reading it through a file-reading method, instead of hardcoding them directly in the script
class LoginPage(BasePage):
     # Defining constructor to initialize driver and locator utility like this
     def __init__(self,driver,locator_utility):
         super().__init__(driver)
         self.locators=locator_utility
         self.wait=WebDriverWait(self.driver,15)

     # Method to locate and enter the username using provided locator and value
     def enter_username(self,username):
         try:
            username_by,username_value=self.locators["username_input"]
            u_input=self.wait.until(
                expected_conditions.presence_of_element_located((getattr(By, username_by.upper()), username_value)))
            if username:
                u_input.send_keys(username)
            else:
                print("No Value for Username")
         except TimeoutException:
            print("Username element not Found")

     # Method to locate and enter the password using provided locator and value
     def enter_password(self,password):
         try:
             pwd_by, pwd_value = self.locators["password_input"]
             pwd_input = self.wait.until(
                 expected_conditions.visibility_of_element_located(
                     (getattr(By, pwd_by.upper()), pwd_value)))
             if password:
                 pwd_input.send_keys(password)
             else:
                 print("No Value for Password")
         except TimeoutException:
             print("Password element not Found")

     # Method to locate and click on login button
     def click_login(self):
         try:
             login_btn_by, login_btn_value = self.locators["login_btn"]
             login_element=self.wait.until(
                 expected_conditions.element_to_be_clickable(
                     (getattr(By,login_btn_by.upper()),login_btn_value)))
             if login_element.is_enabled():
                 login_element.click()
             else:
                 print("Login button is not enabled")
         except TimeoutException:
             print("Login element not found")

     # Method to locate error messages using provided locator and value
     def error_messages(self):
         try:
            err_message_by,err_message_value=self.locators["error_message"]
            error_element=self.wait.until(
                expected_conditions.visibility_of_element_located(
                    (getattr(By,err_message_by.upper()),err_message_value)))
            if error_element.is_displayed():
                error_text=error_element.text
                print(f"Error message: {error_text}")
                return error_text
            else:
                print("No error message found")
         except TimeoutException:
            print("No Error Element found")

     # Method to use in test logic that fetch the page url for assertion
     def get_current_url(self):
         actual_url=self.driver.current_url
         return actual_url

     def read_login_element(self):
         login_by, login_value = self.locators["login_element"]
         login_elem =self.wait.until(
             expected_conditions.visibility_of_element_located(
                 (getattr(By,login_by.upper()),login_value)
             )
         )

