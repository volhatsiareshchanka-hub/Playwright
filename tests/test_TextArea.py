from playwright.sync_api import Page, expect
import time

def test_open_google(page: Page) -> None:
    page.goto("https://www.qa-practice.com/")
    time.sleep(2)


 # Textarea

    page.get_by_role("link", name="Text input").click()
    page.get_by_role("link", name="Text area").click()
    page.locator('#req_header').click()
    time.sleep(2)
    page.get_by_role("button", name="Submit").click()
    input_field = page.locator("#id_text_area")
    input_field.click()
    input_field.fill('Writing tests via Playwright')
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("You entered Writing tests via Playwright")).to_be_visible()
    time.sleep(2)


# Multiple text areas
    page.get_by_role("link", name="Multiple textareas").click()
    page.locator("#req_header").click()

    second = page.locator("#id_second_chapter")
    second.click()
    second.fill("Writing tests via Playwright")
    page.get_by_role("button", name="Submit").click()

    expect(second).to_have_value("Writing tests via Playwright")
    time.sleep(2)

