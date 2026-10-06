from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_to_cart(inventory: InventoryPage):

    inventory.check_cards_info()

    inventory.expect_opened()
    inventory.add_product_to_cart("Sauce Labs Backpack")
