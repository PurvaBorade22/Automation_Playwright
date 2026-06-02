import pytest 
from playwright.sync_api import Page ,expect

def test_single_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    # 3 methods to select a single dropdown
    
    # page.locator("#country").select_option("India") # 1 by label
    # page.locator("#country").select_option(label="India") 
    
    # page.locator("#country").select_option(value="germany")  # 2 by value
    
    page.locator("#country").select_option(index=3)
    
    page.wait_for_timeout(3000)
        