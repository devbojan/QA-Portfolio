from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"
        self.success_message = ".flash.success"
        self.error_message = ".flash.error"

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.locator(self.login_button).click()

    def is_login_successful(self):
        return self.page.locator(self.success_message).is_visible()

    def is_login_failed(self):
        return self.page.locator(self.error_message).is_visible()
