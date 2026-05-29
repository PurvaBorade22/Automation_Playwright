# //button[text()='START' or text()='STOP']
# //button[@name='start' or @name='stop']
# //button[contains(@name,'st')]
# //button[starts-with(@name,'st')]

import pytest

from playwright.sync_api import Page,expect


def test_dynamic_XPaths(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    
    for i in range(5):
        button = page.locator("//button[text()='START' or text()='STOP']")
        button.click()
        page.wait_for_timeout(3000)
        
        