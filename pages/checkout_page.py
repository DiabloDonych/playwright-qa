from playwright.sync_api import Page, expect


class CheckOutPage:
    def __init__(self, page : Page):
        self.page = page


    def checkout(self):
        self.page.locator('[data-test="checkout"]').click() 

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.locator('[data-test="firstName"]').fill(first_name)
        self.page.locator('[data-test="lastName"]').fill(last_name)
        self.page.locator('[data-test="postalCode"]').fill(postal_code)
        self.page.locator('[data-test="continue"]').click()

    def expect_product_in_overview(self, product_name):
        expect(self.page.get_by_text(product_name, exact=True)).to_be_visible()


    def finish_checkout(self):
        self.page.locator('[data-test="finish"]').click()
        expect(self.page.locator('[data-test="complete-header"]')).to_be_visible()

    def expect_true_checkout_info(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")


    def expect_false_checkout_info(self):
        expect(self.page.locator("[data-test=\"error\"]")).to_be_visible()


        