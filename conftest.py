import pytest
from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage


@pytest.fixture
def successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    yield page


@pytest.fixture
def inventory(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    return InventoryPage(page)


@pytest.fixture
def cart_page(inventory: InventoryPage):

    inventory.add_product_to_cart("Sauce Labs Backpack")

    return CartPage(inventory.page)


@pytest.fixture
def checkout_page(inventory: InventoryPage):
    login_page = LoginPage(inventory)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return CheckOutPage(cart_page.page)