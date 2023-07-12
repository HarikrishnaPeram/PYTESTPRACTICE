import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_etoe(self):
        self.driver.implicitly_wait(7)
        ValidateYourDetails=self.driver.find_element(By.ID,"Recheck")

        ValidateYourDetails.click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//input[@id='opt_cat'])[4]").click()

        alert = self.driver.switch_to.alert
        alert.accept()

        self.driver.find_element(By.XPATH, "//input[@id='optdisability'][1]").click()
        self.driver.find_element(By.XPATH,"//input[@id='optriots'][1]").click()
        self.driver.find_element(By.XPATH, "//input[@id='optexservice'][1]").click()
        Dropdown1 = Select(self.driver.find_element(By.ID,"seldobday"))
        Dropdown1.select_by_index(4)
        Dropdown2 = Select(self.driver.find_element(By.ID, "seldobmon"))
        Dropdown2.select_by_index(4)
        Dropdown2 = Select(self.driver.find_element(By.ID, "seldobyear"))
        Dropdown2.select_by_index(5)
        self.driver.find_element(By.XPATH,"//input[@id='optsex'][1]").click()
        Dropdown3 = Select(self.driver.find_element(By.ID, "txtstate"))
        Dropdown3.select_by_index(2)
        self.driver.find_element(By.ID,"same_presentadd").click()
        #Dropdown4 = Select(self.driver.find_element(By.ID, "gstState"))
        #Dropdown4.select_by_index(0)
        #self.driver.find_element(By.ID,"FinalSubmit").click()







