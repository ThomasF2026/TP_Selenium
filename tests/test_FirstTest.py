import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..")) # .. on remontepip
from helpers.BaseTest import BaseTest
from pages.HomePage import HomePage
from pageFragments.HeaderPageFragment import HeaderPageFragment
from time import sleep
from pages.ProductListPage import ProductListPage
from pages.ProductPage import ProductPage
from pages.PopUpPage import PopUpPage
from pages.CheckoutPage import CheckoutPage  
from pages.GuestCheckoutPage import GuestCheckoutPage


class Test_FirstTest(BaseTest): # héritage

    @pytest.mark.test_MyFirstTest
    def test_MyFirstTest(self):
        self.open_application()

        Home_Page = HomePage(self.driver)
        Home_Page.is_page_visible("Your Store")

        header = HeaderPageFragment(self.driver)
        header.select_menu()
        header.select_subMenu()

        ProductList = ProductListPage(self.driver)
        ProductList.clickOn_FilterOnStock()
        sleep(3)
        ProductList.select_ProductItem()

        AddToCart = ProductPage(self.driver)
        AddToCart.clickOn_AddToCartButton()
        
        ViewCartButton = PopUpPage(self.driver)
        ViewCartButton.clickOn_ViewCartButton()
        sleep(2)
        CheckoutButton = CheckoutPage(self.driver)
        CheckoutButton.clickOn_CheckoutButton()

        sleep(2)
        GuestCheckout = GuestCheckoutPage(self.driver)
        GuestCheckout.select_GuestCheckout()
        GuestCheckout.fill_FirstName("Michel")
        GuestCheckout.fill_LastName("Célebrésil")
        GuestCheckout.fill_Email("Mimiche@hotmail.fr")
        GuestCheckout.fill_Telephone("06 06 06 06 06")
        GuestCheckout.fill_Company("Jebrûlelepatronat")
        GuestCheckout.fill_Address1("1312 rue du syndicat")
        GuestCheckout.fill_Address2("1312 rue de Poesie Zero")








