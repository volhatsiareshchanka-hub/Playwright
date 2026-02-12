from playwright.sync_api import Page, expect
import time

def test_open_google(page: Page) -> None:
    page.goto("https://www.qa-practice.com/")
    time.sleep(2)

# Single checkbox
    page.get_by_role("link", name="Text input").click()
    page.get_by_role("link", name="Checkbox").click()
    page.locator('#req_header').click()
    time.sleep(2)
    page.locator('#id_checkbox_0').check()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Selected checkboxes: select me or not")).to_be_visible()
    time.sleep(2)

# Checkboxes
    page.get_by_role("link", name="Checkboxes").click()
    page.locator('#req_header').click()
    time.sleep(2)
    page.locator('#id_checkboxes_2').check()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Selected checkboxes: three")).to_be_visible()
    time.sleep(2)



