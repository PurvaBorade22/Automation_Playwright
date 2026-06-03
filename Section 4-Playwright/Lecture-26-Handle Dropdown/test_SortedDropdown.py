import pytest

from playwright.sync_api import Page, expect

def test_sorteddropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    dropdown_options= page.locator("#colors>option") #unsorted
    # dropdown_options = page.locator("#animals>option") #sorted
    
    options_text=[text.strip() for text in dropdown_options.all_text_contents()]
    
    original_list = options_text.copy()
    sorted_list = sorted(options_text)
    
    print("Original list:",original_list)
    print("Sorted list:",sorted_list)
    
    if original_list==sorted_list:
        print("List is sorted....")
    else:
        print("List is not sorted...")
    
    