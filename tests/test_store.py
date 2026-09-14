import re
from playwright.sync_api import Page, expect

def test_open_site(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")

def test_get_started_link(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")

    page.get_by_role("img", name="Striped top").click()

    expect(page.get_by_role("button", name="Add to Cart")).to_be_visible()


def test_price(page: Page):
    page.goto("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")

    expect(page.get_by_role("heading", name="£50.00")).to_be_visible()


def test_name_product(page: Page):
    page.goto("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")

    expect(page.get_by_role("heading", name="Striped top")).to_be_visible()


def test_active_click(page: Page):
    page.goto("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")

    button = page.get_by_role("button", name="Add to Cart")
    expect(button).to_be_enabled()


def test_url(page: Page):
    page.goto("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")

    expect(page).to_have_url(re.compile(r".*/collections/frontpage/products/striped-top"))


def test_cart_click(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")
    
    page.get_by_role("img", name="Striped top").click()

    expect(page).to_have_url("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")
    

def test_add_to_cart(page: Page):
    page.goto("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")

    page.get_by_role("button", name="Add to Cart").click()

    expect(page.get_by_role("link", name = "My Cart (1)")).to_be_visible()


def test_search(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")

    page.get_by_placeholder("Search").fill("Striped top")

    page.get_by_role("link", name="Striped top").click()

    page.get_by_role("heading", name="Striped top").click()

    expect(page).to_have_url("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")