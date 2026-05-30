import pytest

from playwright.sync_api import Page,expect

def test_RadioButton(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    male_radio = page.locator("#male")
    
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()
    
    # male radio button should not be checked ( default)
    expect(male_radio).not_to_be_checked()
    
    #check radio button
    male_radio.check()
    
    #checked the radio button
    expect(male_radio).to_be_checked()
    
    page.wait_for_timeout(5000)