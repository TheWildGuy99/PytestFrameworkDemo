import time

from page_locators.home_pagelocators import HomePage
from utilities.genericUtils import GenericUtils

class HomePageMethods(GenericUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def choose_service(self):
        self.click(HomePage.buy_phone)
        time.sleep(5)


