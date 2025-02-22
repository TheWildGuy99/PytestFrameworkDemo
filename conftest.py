import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#Test Controls
region_type = 'staging'
headless = False
resolution = '1920x1080'

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default = "chrome"
    )

def get_region(region):
    region_link = ""
    if region == 'staging':
        region_link =  "https://www.cashify.in"
    elif region== 'test':
        region_link = "https://www.cashify.in"
    return region_link

@pytest.fixture(scope= "class")
def invoke_browser(request):
    browser = request.config.getoption("browser_name")

    if browser == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        options.add_argument(f"--window-size={resolution}")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        options.add_argument(f"--window-size={resolution}")
        driver = webdriver.Firefox(options=options)

    driver.get(get_region(region_type))
    driver.delete_all_cookies()
    request.cls.driver = driver
    yield
    driver.quit()
