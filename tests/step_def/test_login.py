# Importing needed packages
import time
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Task_18.pages.base_page import BasePage
from Task_18.pages.dashboard_page import Dashboard
from Task_18.pages.login_page import LoginPage

# Linking the feature file to the step definitions for test execution
scenarios("test_login.feature")

# step to launch the application and navigate to the login page using the given URL
@given('The user is on the login page')
def launch_application(driver,url_utility):
    base_object=BasePage(driver)
    base_object.navigate(url_utility,"login_url")
    time.sleep(3)

# Step to enter the provided username and password on the login page
@when(parsers.re(r'^The user enters (?P<username>.*) and (?P<password>.*) and login'))
def enter_credentials(driver,locator_utility,username,password):
    login_object=LoginPage(driver,locator_utility)
    login_object.enter_username(username)
    login_object.enter_password(password)

# Step to click on login
@when('Click on login button')
def click_functions(driver,locator_utility):
    login_object=LoginPage(driver,locator_utility)
    login_object.click_login()

# Step to validate whether the user lands on the dashboard
@then(parsers.cfparse('The valid user gets {result} and land on Dashboard'))
def user_landed(driver, result, locator_utility,dashboard_utility,url_utility):
    dashboard_object=Dashboard(driver,dashboard_utility)
    login = LoginPage(driver, locator_utility)
    if result=="Dashboard":
        pop_by, pop_value = locator_utility["pop_up"]
        pop_element = WebDriverWait(driver,10).until(
                    expected_conditions.visibility_of_element_located((getattr(By, pop_by.upper()), pop_value)))
        pop_element.click()
        dashboard_object.dashboard_functionality()
        time.sleep(5)
        print("Logged in to dashboard")
        actual_url = login.get_current_url()
        expected_login_url = url_utility["login_url"]
        assert actual_url == expected_login_url
        print("Successfully Logged out")
    else:
        print("Invalid User")

# Step to validate whether the invalid user is not landed on dashboard and received the error message
@then(parsers.cfparse('The Invalid user gets {result} and login error'))
def invalid_user(driver,result,locator_utility):
    login = LoginPage(driver, locator_utility)
    if result != "Dashboard":
        error_text = login.error_messages()
        assert result == error_text, f"Expected error {result},Actual Error {error_text}"
    else:
        print("No error message found")















