from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class GenericUtils:

    def __init__(self,driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def fill_input(self, locator,value):
        self.driver.find_element(By.XPATH, locator).send_keys(value)

    def clear_textbox(self,locator):
        self.driver.find_element(By.XPATH, locator).clear()

    def get_xpath_locator(self,locator):
        return self.driver.find_element(By.XPATH, locator)

    def drag_and_drop(self,source,target):
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(source, target).perform()

    def accept_alert(self):
        ''''''

    def dismiss_alert(self):
        ''''''



