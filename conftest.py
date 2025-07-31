# importing needed packages
import json
import os.path
import pytest
from selenium import webdriver

# This fixture sets up a Chrome browser with notifications disabled.
# It returns the driver for use in tests.
@pytest.fixture
def driver():
    option=webdriver.ChromeOptions()
    option.add_argument("--disable-notifications")
    driver=webdriver.Chrome(option)
    driver.maximize_window()
    return driver

# This fixture is used to end the test run sessions
@pytest.fixture(autouse=True)
def tear_down(driver):
    yield driver
    driver.quit()

# Reading config.json contains environment settings.
def load_config():
    config_path=os.path.join(os.path.dirname(__file__),'config\\config.json')
    with open(config_path,'r') as file_path:
        return json.load(file_path)

# Reading the test_data.json, which contains URL and Error message in the zenportal.
# This method is to read only the URL dictionary in the json file
def get_test_data():
    test_data_path=os.path.join(os.path.dirname(__file__),"utility\\test_data.json")
    with open(test_data_path,'r') as file_path:
        url=json.load(file_path)["URL"]
        return url

# Reading the locators.json, that contains login locators XPATH.
def get_locator():
    locator_path=os.path.join(os.path.dirname(__file__),"utility\\locators.json")
    with open(locator_path,'r') as file_path:
        locators_data=json.load(file_path)["locators"]
        return locators_data

# Reading the dashboard_locators.json, that contains dashboard elements locators.
def get_dash_locator():
    dashboard_path=os.path.join(os.path.dirname(__file__),"utility\\dashboard_locators.json")
    with open(dashboard_path,'r') as file_path:
        dashboard_data=json.load(file_path)["locators"]
        return dashboard_data

# fixture to call the config method around the project.
@pytest.fixture(scope="session")
def config():
    return load_config()

# fixture to call the get_test_data method to use it around the project.
@pytest.fixture(scope="session")
def url_utility():
    return get_test_data()

# fixture to call the get_locator method to use it around the project.
@pytest.fixture(scope="session")
def locator_utility():
    return get_locator()

# Fixture to call the get_dashboard_locator method to use it in the project.
@pytest.fixture
def dashboard_utility():
    return get_dash_locator()