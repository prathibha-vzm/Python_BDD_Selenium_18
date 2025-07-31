# Importing the needed packages
from selenium.common import TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Task_18.pages.base_page import BasePage

# This class inherits baseclass and used to locate the elements in dashboard page after login and to click on logout

class Dashboard(BasePage):
    # Defining constructor to initialize driver and dashboard utility like this
    def __init__(self,driver,dashboard_utility):
        super().__init__(driver)
        self.driver=driver
        self.locators=dashboard_utility
        self.wait = WebDriverWait(self.driver, 10)

    # This method is to locate the elements
    def dashboard_functionality(self):
        try:
            name_by, name_value = self.locators["name_element"]
            read_name = self.wait.until(
                expected_conditions.visibility_of_element_located((getattr(By, name_by.upper()), name_value)))
            print(f"Welcome{read_name.text}")
            arrow_by,arrow_value=self.locators["arrow_element"]
            arrow_element_click=self.wait.until(
                expected_conditions.element_to_be_clickable(
                    (getattr(By,arrow_by.upper()),arrow_value)))
            if arrow_element_click:
                arrow_element_click.click()
            else:
                print("arrow not found")
            logout_by,logout_value=self.locators["logout_element"]
            logout_element_click=self.wait.until(
                expected_conditions.element_to_be_clickable(
                    (getattr(By,logout_by.upper()),logout_value)))
            if logout_element_click:
                logout_element_click.click()
            else:
                print("No logout element found")
        except (TimeoutException,ElementNotVisibleException):
            print("Dashboard Elements not found")


