from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.open_cart = page.locator('[data-test="shopping-cart-link"]')
        self.empty_cart = page.locator('[data-test="inventory-item"]')


    def open(self):
        self.open_cart.click()


    def expect_product_added(self, product_name):
        expect(self.page.get_by_text(product_name, exact=True)).to_be_visible()


    def expect_cart_empty(self):
        expect(self.empty_cart).to_have_count(0)


    def remove_product_from_cart(self, product_name):
        product_id = product_name.lower().replace(" ", "-")
        
        self.page.locator(f'[data-test="remove-{product_id}"]').click()