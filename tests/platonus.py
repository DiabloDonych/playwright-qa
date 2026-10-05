from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(
        "http://127.0.0.1:9222"
    )

    context = browser.contexts[0]
    page = context.pages[0]

    print("URL:", page.url)

    # Поля формы
    login = page.locator("#login_input")
    language = page.locator("#language")
    password = page.locator("#pass_input")
    schedule = page.locator('div.d-flex.align-items-center').get_by_text("Расписание", exact=True)

    # Язык
    language.select_option("1")

    # Логин
    login.fill("Логин")

    # Пароль
    password.fill("Пароль")

    print("Логин и пароль введены")

    # Кнопка "Войти"
    login_button = page.locator("button").filter(has_text="Войти")

    print("Кнопок Войти:", login_button.count())

    # Нажимаем
    login_button.click()

    print("Кнопка Войти нажата")

    schedule.wait_for(state="visible",timeout=60000)

    print("Видно расписание")

    schedule.click()

    # Ждём изменения страницы
    page.wait_for_timeout(3000)

    print("После входа URL:", page.url)

    input("Проверь браузер. Нажми Enter для завершения...")