import pytest
from page_methods.home_pagemethods import HomePageMethods


@pytest.mark.usefixtures("invoke_browser")
class TestClass:

    def test_choose_service(self):
        self.home = HomePageMethods(self.driver)

        self.home.choose_service()


