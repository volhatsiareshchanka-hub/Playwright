from playwright.sync_api import Page, expect
import time

def test_open_google(page: Page) -> None:
    page.goto("https://www.qa-practice.com/")
    time.sleep(2)

# Simple button
    page.get_by_role("link", name="Text input").click()
    page.get_by_role("link", name="Buttons").click()
    page.locator('#req_header').click()
    time.sleep(2)
    page.get_by_role("button", name="Click").click()
    expect(page.get_by_text("Submitted")).to_be_visible()
    time.sleep(2)

# Looks like a button
    page.get_by_role("link", name="Looks like a button").click()
    page.locator('#req_header').click()
    time.sleep(2)
    page.get_by_role("link", name="Click").click()
    expect(page.get_by_text("Submitted")).to_be_visible()
    time.sleep(2)

# Disabled
    page.get_by_role("link", name="Disabled").click()
    page.locator('#req_header').click()
    page.locator("#id_select_state").select_option('Enabled')
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Submitted")).to_be_visible()
    time.sleep(2)





