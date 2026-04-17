from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
 
class PopUpPage():
 
    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_ViewCartButton = '//a[contains(text(),"View Cart ")]'
 
    def clickOn_ViewCartButton(self):
        c_btn_ViewCartButton = self.driver.find_element(By.XPATH,self.btn_ViewCartButton) 
        c_btn_ViewCartButton.click()