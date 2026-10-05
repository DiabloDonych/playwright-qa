from playwright.sync_api import Page, Playwright, Browser, expect
from pages.login_page import LoginPage
import pytest



def test_login(page : Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    login_page.expect_successful_login()

def test_invalid_login(page : Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce123")
    login_page.expect_invalid_login()

def test_locked_out_user(page : Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    login_page.expect_locked_out_user()