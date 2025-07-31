# Python_BDD_Selenium
## BDD, selenium, Allure, POM, Pytest, DDTF, Explicit wait, Exception handling
## Testing Tool used - Selenium
## Test Structure -Given-When-And-Then with AAA
## Frameworks
 ### DDTF (Data Driven Testing Framework) to store test data in a seperate Json file for better data management.
 ### Pytest as Test runner
 ### POM (Page Object Model)
## BDD (Behavior-Driven Development):
* Implemented using pytest-bdd. Test scenarios are written in .feature files using Given-When-Then syntax for better readability and collaboration.
## Wait - Used Explicit wait to handle elements visibility.
## Exception handling - Handled the TimeoutError for uniterrupted test runs.
## OOPS concept
## Project Structure:- POM
1. Pages - The Login page elements are located here and values are passed from test logic.
2. Tests - Contains step definitions mapped to Gherkin steps.
3. conftest - To create the environment to run the test. This file is located under test package
4. Utility - This package contains Json files that contains locators for the elements.
5. requiremenets.txt - This file contains the packages needed for this project
6. pytest.ini - Configuration file to customize Pytest options.
7. config -  Configuration files to set up environment settings
8. Allure reports - This directory contais report.html generated after test execurtion and screenshots captured during test runs.
  ## Steps to run the test and generate Allure report
  1. pytest tests/ --alluredir=allure-results -m login_tests
  2. allure generate allure-results -o allure-report --clean
  3. allure open allure-report
