import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.parametrize("first_name, last_name, postal_code, should_pass",
    [
    ("John", "Doe", "12345", True),               
    ("", "Doe", "12345", False),
    ("Jane", "", "54321", False),
    ("Alice", "Johnson", "", False),
    ]
)
def test_checkout(page : Page, first_name, last_name, postal_code, should_pass):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckOutPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.expect_opened()
    inventory_page.add_product_to_cart("Sauce Labs Backpack")   
    
    cart_page.open()
    cart_page.expect_product_added("Sauce Labs Backpack")
    
    checkout_page.checkout()
    checkout_page.fill_checkout_info(first_name, last_name, postal_code)
    
    if should_pass:
        checkout_page.expect_true_checkout_info()
        checkout_page.expect_product_in_overview("Sauce Labs Backpack")
        checkout_page.finish_checkout()
    else:
        checkout_page.expect_false_checkout_info()


def test_fixture_checkout(successful_login: Page):
    inventory_page = InventoryPage(successful_login)
    cart_page = CartPage(successful_login)
    checkout_page = CheckOutPage(successful_login)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page.open()
    cart_page.expect_product_added("Sauce Labs Backpack")

    checkout_page.checkout()
    checkout_page.fill_checkout_info(
        "John",
        "Doe",
        "12345"
    )
    checkout_page.expect_product_in_overview(
        "Sauce Labs Backpack"
    )
    checkout_page.finish_checkout()