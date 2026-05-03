from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in page.url

        page.screenshot(path="screenshots/login-success.png")

        browser.close()
