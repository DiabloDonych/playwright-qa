from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_cart(cart_page: CartPage):  

    cart_page.open()
    cart_page.expect_product_added("Sauce Labs Backpack")
    cart_page.remove_product_from_cart("Sauce Labs Backpack")

