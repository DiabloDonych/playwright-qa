import pytest
import re
from playwright.sync_api import Page, expect

@pytest.fixture
def main_page(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")
    return page


def test_striped_top(main_page):

    expect(main_page.get_by_role("img", name="Striped top")).to_be_visible()



