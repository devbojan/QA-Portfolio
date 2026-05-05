import pytest
import os
import json
from playwright.sync_api import sync_playwright

BASE_URL = "https://jsonplaceholder.typicode.com/"


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def api(playwright_instance):
    context = playwright_instance.request.new_context(
        base_url=BASE_URL
    )
    yield context
    context.dispose()


@pytest.fixture
def page(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    page = browser.new_page()
    yield page
    browser.close()


# 📸 Screenshot na FAIL sa JSON response
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            file_path = f"screenshots/{item.name}.png"

            response = getattr(item.function, "api_response", None)

            if response:
                try:
                    data = response.json()
                    formatted_json = json.dumps(data, indent=2)
                except:
                    formatted_json = response.text()
            else:
                formatted_json = "No response captured"

            html_content = f"""
            <html>
                <body style="font-family: monospace; background-color: #111; color: #0f0;">
                    <h2>Test Failed - API Response</h2>
                    <pre>{formatted_json}</pre>
                </body>
            </html>
            """

            page.set_content(html_content)
            page.screenshot(path=file_path)

            print(f"\n📸 Screenshot saved: {file_path}")