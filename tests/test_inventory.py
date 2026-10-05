from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_to_cart(page: Page):
    
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.check_cards_info

    inventory_page.expect_opened()
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
