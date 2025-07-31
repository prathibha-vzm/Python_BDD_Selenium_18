#Base page is to visit the login page
class BasePage:
      def __init__(self,driver):
          self.driver=driver
      #This method is to navigate through pages. Passing url_utility method, and passing key to send the values
      def navigate(self,url_utility,key):
          self.driver.get(url_utility[key])