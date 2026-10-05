from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import pytest



def test_cart(successful_login: Page):
    inventory_page = InventoryPage(successful_login)
    cart_page = CartPage(successful_login)


    inventory_page.check_cards_info()
    inventory_page.expect_opened()
    inventory_page.add_product_to_cart("Sauce Labs Backpack")   


    cart_page.open_cart()
    cart_page.expect_product_added("Sauce Labs Backpack")
    cart_page.remove_product_from_cart("Sauce Labs Backpack")

