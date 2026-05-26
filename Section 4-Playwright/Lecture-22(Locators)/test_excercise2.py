import time

from playwright.sync_api import Page, expect

def test_verify_playwright_locators(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.wait_for_timeout(10000)
    
    # 1) locate image by alt
    expect(page.get_by_alt_text("logo image")).to_be_visible()
    
    # 2) locate by text(headings)
    expect(page.get_by_text("List item 1")).to_be_visible()
    expect(page.get_by_text("List item 2 with")).to_be_visible()   
    expect(page.get_by_text("Special: Unique text identifier")).to_be_visible()
    
    # 3) locate by role 
    expect(page.get_by_role("Button", name = "Primary Action")).to_be_visible()
    expect(page.get_by_role("Button", name = "Toggle Button")).to_be_visible()
    expect(page.get_by_role("Button", name = "Div with button role")).to_be_visible()
    
    # 4) locate by label
    page.get_by_label("Email Address:").fill("purva@gmail.com")
    page.get_by_label("Password:").fill("Purva@123")
    page.get_by_label("Your Age:").fill("21")
    page.get_by_label(" Standard").check()
    page.get_by_label(" Express").check()
    
    # 5) page. get_by_placeholder()
    page.get_by_placeholder("Enter your full name").fill("Purva borade")
    page.get_by_placeholder("Phone number (xxx-xxx-xxxx)").fill("123-456-7890")
    page.get_by_placeholder("Type your message here...").fill("This is purva here")
    page.get_by_placeholder("Search products...").fill("PW book")
    page.get_by_role("button", name = "Search").click()