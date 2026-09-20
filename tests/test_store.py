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



def test_label_search(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")

    page.get_by_placeholder("Search").fill("Striped top")

    page.get_by_role("header", name="Search Results")



def test_add_to_cart_by_locator(page: Page):
    page.goto("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")

    button_id = page.locator("#add")
    button_class = page.locator(".btn.add-to-cart")
    input_tag = page.get_by_role("button", name="Add to Cart")

    expect(button_id).to_be_visible()
    expect(button_class).to_be_visible()
    expect(input_tag).to_be_visible()



def test_count_inputs(page: Page):
    page.goto("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")

    inputs = page.locator("input")

    print(inputs.count())



def test_filter(page: Page):
    page.goto("https://sauce-demo.myshopify.com")

    products = page.locator(".animated.fadeInUpBig").filter(has_text="Striped top")

    expect(products).to_be_visible()



def test_click(page: Page):
    page.goto("https://sauce-demo.myshopify.com")

    page.get_by_role("img", name="Striped top").click()

    expect(page).to_have_url("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")
    expect(page.get_by_role("heading", name="Striped top")).to_be_visible()



def test_search(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")

    page.locator(".search").fill("Striped top")

    page.get_by_role("header", name="Search Results")

    page.locator(".animated.fadeInUpBig").filter(has_text = "Striped top").click()

    expect(page).to_have_url("https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top")



def test_not_visible(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")

    page.locator(".search").fill("not_existing_product")

    expect(page.locator(".animated.fadeInUpBig").filter(has_text = "not_existing_product")).not_to_be_visible()
    


def test_dropdown(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")

    page.get_by_role("img", name="Noir jacket").click()

    page.locator(".single-option-selector[data-option = 'option1']").select_option("S")

    expect(page.locator(".single-option-selector[data-option = 'option1']")).to_have_value("S")



def test_press(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")

    page.locator(".search").fill("Noir jacket")

    page.locator(".animated.fadeInUpBig").filter(has_text = "Noir jacket").click()

    expect(page).to_have_url("https://sauce-demo.myshopify.com/collections/frontpage/products/noir-jacket")



def test_scenario(page : Page):
    page.goto("https://sauce-demo.myshopify.com/")

    page.locator(".animated.fadeInUpBig").filter(has_text = "Noir jacket").click()

    expect(page).to_have_url("https://sauce-demo.myshopify.com/collections/frontpage/products/noir-jacket")

    page.locator(".single-option-selector[data-option = 'option1']").select_option("S")

    expect(page.locator(".single-option-selector[data-option = 'option1']")).to_have_value("S")

    page.get_by_role("button", name="Add to Cart").click()

    expect(page.get_by_role("link", name = "My Cart (1)")).to_be_visible()

    page.get_by_role("link", name = "My Cart (1)").click()

    page.get_by_role("link", name="Check Out").click()

    expect(page.get_by_role("link", name="Noir jacket - S / Blue")).to_be_visible()



def test_plus():
    assert 1 + 1 == 2



def test_registration(page: Page):

    

    page.context.tracing.start(screenshots=True, snapshots=True)

    page.goto("https://playwrightlab.github.io/index.html")

    page.pause()

    cookie = page.get_by_test_id("cookie-accept")
    name = page.locator("#fullName")
    email = page.locator("#email")
    password = page.get_by_placeholder("Min 8 characters")
    phone = page.locator("#phone")
    country = page.locator("#country")
    male = page.locator("#labelMale")
    js_checkbox = page.locator("#checkJs")
    bio = page.locator("#bio")
    terms = page.locator("#terms")

    
    cookie.click()

    page.screenshot(path="registration.png",full_page=True)

    name.fill("Alex")
    expect(name).to_have_value("Alex")

    email.fill("Alex@gmail.com")
    expect(email).to_have_value("Alex@gmail.com")

    email.screenshot(path="email_field.png")

    password.fill("123123")
    expect(password).to_have_value("123123")

    phone.fill("+1234567890")
    expect(phone).to_have_value("+1234567890")

    country.select_option("br")
    expect(country).to_have_value("br")

    male.check()
    expect(male).to_be_checked()

    js_checkbox.check()
    expect(js_checkbox).to_be_checked()

    bio.fill("I am a QA engineer")
    expect(bio).to_have_value("I am a QA engineer")

    terms.check()
    expect(terms).to_be_checked()

    page.context.tracing.stop(path="trace.zip")


def test_slider(page: Page):
    page.goto("https://playwrightlab.github.io/index.html")

    slider = page.locator("#volumeSlider")
    slider.fill("75")
    expect(slider).to_have_value("75")



