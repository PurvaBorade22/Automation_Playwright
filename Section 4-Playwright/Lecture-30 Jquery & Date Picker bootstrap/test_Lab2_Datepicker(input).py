import pytest

from playwright.sync_api import Page,expect

def test_Lab2_DatePicker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#start-date").fill("2026-06-18") 
    page.locator("#end-date").fill("2026-06-25")

    #assertion 
    expect(page.locator("#start-date")).to_have_value("2026-06-18")
    expect(page.locator("#end-date")).to_have_value("2026-06-25")

    #click on button
    page.locator(".submit-btn").click()

    #succssful msg
    success_msg= page.locator(".result")
    expect(success_msg).to_be_visible()

    #print the dates
    print("Start date===>",page.locator("#start-date").input_value())
    print("End Date===>",page.locator("#end-date").input_value())

    page.wait_for_timeout(5000)