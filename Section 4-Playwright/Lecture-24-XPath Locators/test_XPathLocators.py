import pytest
from playwright.sync_api import Page,expect

def test_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    
    # 1) Absoulate xpath
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()
    
    # 2) Relative xpath
    logo = page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()
    page.wait_for_timeout(5000)