from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
 
class ProductPage():
 
    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_addToCartButton = '(//button[contains(@title,"Add to Cart")])[2]'
 
    def clickOn_AddToCartButton(self):
        c_btn_addToCartButton = self.driver.find_element(By.XPATH,self.btn_addToCartButton) 
        c_btn_addToCartButton.click()