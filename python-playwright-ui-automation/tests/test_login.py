from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.open()
        login_page.login("tomsmith", "SuperSecretPassword!")

        assert login_page.is_login_successful()

        page.screenshot(path="screenshots/login-success.png")

        browser.close()


def test_login_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.open()
        login_page.login("wrong", "wrong")

        assert login_page.is_login_failed()

        browser.close()
