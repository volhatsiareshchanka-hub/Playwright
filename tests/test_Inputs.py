from playwright.sync_api import Page, expect
import time

def test_open_google(page: Page) -> None:
    page.goto("https://www.qa-practice.com/")
    time.sleep(2)

    page.get_by_role("link", name="Text input").click()
    page.get_by_role("link", name="Inputs").click()
    page.locator('#req_header').click()
    time.sleep(2)
    input_field = page.locator("#id_text_string")
    input_field.click()
    input_field.fill('Playwright')
    input_field.press("Enter")
    expect(page.get_by_text("Your input was: Playwright")).to_be_visible()
    time.sleep(2)

    page.get_by_role("link", name="Email field").click()
    page.locator('#req_header').click()
    time.sleep(2)
    input_field = page.locator("#id_email")
    input_field.click()
    input_field.fill('volha.tsiareshchanka@gmail.com')
    time.sleep(2)
    input_field.press("Enter")
    expect(page.get_by_text("Your input was: volha.tsiareshchanka@gmail.com")).to_be_visible()
    time.sleep(2)

    page.get_by_role("link", name="Password field").click()
    page.locator('#req_header').click()
    time.sleep(2)
    input_field = page.locator("#id_password")
    input_field.click()
    input_field.fill('Vt12345678!')
    time.sleep(2)
    input_field.press("Enter")
    expect(page.get_by_text("Your input was: Vt12345678!")).to_be_visible()
    time.sleep(2)


