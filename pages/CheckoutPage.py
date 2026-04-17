from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
 
class CheckoutPage():
 
    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_CheckoutButton = '//a[contains(text(),"Checkout")]'
 
    def clickOn_CheckoutButton(self):
        c_btn_CheckoutButton = self.driver.find_element(By.XPATH,self.btn_CheckoutButton) 
        c_btn_CheckoutButton.click()