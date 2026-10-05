from playwright.sync_api import Page, Playwright, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page    

    def open(self):
        self.page.goto("https://www.saucedemo.com/")


    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()


    def expect_successful_login(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")


    def expect_invalid_login(self):
        expect(self.page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()

    
    def expect_locked_out_user(self):
        expect(self.page.get_by_text("Epic sadface: Sorry, this user has been locked out.")).to_be_visible()
