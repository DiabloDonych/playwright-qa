from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = self.page.locator("[data-test = 'inventory_item']")

    def open(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def expect_opened(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")


    def add_product_to_cart(self, product_name):
        product_id = product_name.lower().replace(" ", "-")

        self.page.locator(f'[data-test="add-to-cart-{product_id}"]').click()

    def check_cards_info(self):
        for i in range(self.items.count()):
            item = self._items.nth(i)
            expect(item.locator('[data-test="inventory-item-name"]')).to_be_visible()
            expect(item.locator('[data-test="inventory-item-desc"]')).to_be_visible()
            expect(item.locator('[data-test="inventory-item-price"]')).to_be_visible()
            expect(item.locator(".btn_inventory")).to_be_visible()


