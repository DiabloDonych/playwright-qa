from playwright.sync_api import Page, expect


class CheckOutPage:
    def __init__(self, page : Page):
        self.page = page
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.end_checkout_message = page.locator('[data-test="complete-header"]')
        self.checkout_error = self.page.locator("[data-test=\"error\"]")

    def checkout(self):
        self.checkout_button.click() 

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    def expect_product_in_overview(self, product_name):
        expect(self.page.get_by_text(product_name, exact=True)).to_be_visible()


    def finish_checkout(self):
        self.finish_button.click()
        expect(self.end_checkout_message).to_be_visible()

    def expect_true_checkout_info(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")


    def expect_false_checkout_info(self):
        expect(self.checkout_error).to_be_visible()


        