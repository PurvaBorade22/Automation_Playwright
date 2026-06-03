import pytest 
from playwright.sync_api import Page ,expect

def test_single_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    # 3 methods to select a single dropdown
    
    # page.locator("#country").select_option("India") # 1 by label
    # page.locator("#country").select_option(label="India") 
    
    # page.locator("#country").select_option(value="germany")  # 2 by value
    
    # page.locator("#country").select_option(index=3)
    
    # page.wait_for_timeout(3000)
    
    # print dropdown values in list or individual
    #in list
    dropdown_option = page.locator("#country>option")
    expect(dropdown_option).to_have_count(10)
    
    option_text=[text.strip() for text in dropdown_option.all_text_contents()]
    print(option_text)
    
    # individual
    for option in option_text:
        print(option) 
    
    page.wait_for_timeout(3000)
    
   