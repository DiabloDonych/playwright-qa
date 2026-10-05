from playwright.sync_api import Page, expect, Browser
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage
import pytest


@pytest.fixture
def successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    yield page

