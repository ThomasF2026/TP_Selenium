from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
 
class GuestCheckoutPage():
 
    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.lbl_GuestCheckout = '//label[contains(text(),"Guest Checkout")]'
         self.input_FirstName = '//input[@name="firstname"]'
         self.input_LastName = '//input[@name="lastname"]'
         self.input_Email = '//input[@name="email"]'
         self.input_Telephone = '//input[@name="telephone"]'
         self.input_Company = '//input[@name="company"]'
         self.input_Address1 = '//input[@name="address_1"]'
         self.input_Address2 = '//input[@name="address_2"]'
 
         
    def select_GuestCheckout(self):
        c_lbl_GuestCheckout = self.driver.find_element(By.XPATH,self.lbl_GuestCheckout) 
        c_lbl_GuestCheckout.click()

    def fill_FirstName(self, firstname: str):
        c_input_FirstName = self.driver.find_element(By.XPATH,self.input_FirstName)
        c_input_FirstName.send_keys(firstname)

    def fill_LastName(self, lastname: str):
        c_input_LastName = self.driver.find_element(By.XPATH,self.input_LastName)
        c_input_LastName.send_keys(lastname)

    def fill_Email(self, email: str):
        c_input_Email = self.driver.find_element(By.XPATH,self.input_Email)
        c_input_Email.send_keys(email)

    def fill_Telephone(self, telephone: str):
        c_input_Telephone = self.driver.find_element(By.XPATH,self.input_Telephone)
        c_input_Telephone.send_keys(telephone)

    def fill_Company(self, company: str):
        c_input_Company = self.driver.find_element(By.XPATH,self.input_Company)
        c_input_Company.send_keys(company)

    def fill_Address1(self, address_1: str):
        c_input_Address1 = self.driver.find_element(By.XPATH,self.input_Address1)
        c_input_Address1.send_keys(address_1)

    def fill_Address2(self, address_2: str):
        c_input_Address2 = self.driver.find_element(By.XPATH,self.input_Address2)
        c_input_Address2.send_keys(address_2)