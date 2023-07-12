import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
    driver.get("https://regqc.sifyitest.com/rcfmodec22/reg_details.php?q=NWRiMTRjNWNkYWEwYjA1Y2Q2MDk2ZWU5MGUyNGY1OWZ8MjQ5MDAwMDgz")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()