from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page   
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.invalid_login = page.get_by_text("Epic sadface: Username and password do not match any user in this service")
        self.locked_user = page.get_by_text("Epic sadface: Sorry, this user has been locked out.")

    def open(self):
        self.page.goto("https://www.saucedemo.com/")


    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()


    def expect_successful_login(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")


    def expect_invalid_login(self):
        expect(self.invalid_login).to_be_visible()

    
    def expect_locked_out_user(self):
        expect(self.locked_user).to_be_visible()
