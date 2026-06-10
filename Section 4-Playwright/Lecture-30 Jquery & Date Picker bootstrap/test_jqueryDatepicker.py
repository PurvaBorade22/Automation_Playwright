import pytest

from playwright.sync_api import Page,expect

def test_jquery_date_picker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_picker = page.locator("#datepicker")
    
    #apporach 1
    date_picker.fill("07/23/2004")  #(mm/dd/yyyy)
    expect(date_picker).to_have_value("07/23/2004")

    page.wait_for_timeout(5000)
