import pytest
from playwright.sync_api import Page, expect

def test_multiselect_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    # 3 ways to select value from multiselect dropdown
    
    #page.locator("#colors").select_option(["Red", "Yellow", "Blue"]) # 1 - By Label
    
    # page.locator("#colors").select_option(value=["red","blue","green"]) # 2 - By value(value keyword is mandatory)
    
    page.locator("#colors").select_option(index=[4,2]) # by index
    
    
    page.wait_for_timeout(2000)