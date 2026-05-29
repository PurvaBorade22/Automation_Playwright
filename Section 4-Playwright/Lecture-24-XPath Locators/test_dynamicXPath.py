# XPath
# //button[text()='START' or text()='STOP']
# //button[@name='start' or @name='stop']
# //button[contains(@name,'st')]
# //button[starts-with(@name,'st')]

import pytest
import re

from playwright.sync_api import Page,expect


# def test_dynamic_element_XPaths(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    
#     for i in range(5):
#         button = page.locator("//button[text()='START' or text()='STOP']")
#         button.click()
#         page.wait_for_timeout(3000)
        
        
   # using CSS locator..................    
# button[name='start'],button[name='stop']
# button[name^='st']     # equals to starts-with() in xpath
# button[name*='st']     # eqauals to contains() in xpath
     
# def test_dynamic_element_css(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    
#     for i in range(5):
#         button = page.locator("button[name^='start'], button[name='stop']")
#         button.click()
#         page.wait_for_timeout(3000)


# using playwright locator.......... 
# page.get_by_role("button",name=re.compile(r'ST.*'))


def test_dynamic_element_css(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    
    for i in range(5):
        button = page.get_by_role("button", name=re.compile(r'ST.*'))
        button.click()
        page.wait_for_timeout(3000)