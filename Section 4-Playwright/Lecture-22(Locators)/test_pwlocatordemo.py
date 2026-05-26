import time
import re

from playwright.sync_api import Page, expect

def test_verify_locator(page:Page):
    # page.goto("https://demo.nopcommerce.com/")
    # page.wait_for_timeout(5000) #5000 ms = 5 secs 
    
    # # 1) page.get_by_alt_text
    # logo=page.get_by_alt_text("nopCommerce demo store")
    # expect(logo).to_be_visible()
  
    
    # # # 2) page.get_by_text
    expect(page.get_by_text("Welcome to our store")).to_be_visible()    #full match
    expect(page.get_by_text("Welcome")).to_be_visible()                  #partial match
    expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()             #regular expression

    # 3) page.get_by_role
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(5000)  # 500 ms = 5 secs
    expect(page.get_by_role("heading",name="Register")).to_be_visible()
   
    # 4) page.get_by_label()
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.get_by_label("First Name:").fill("Purva")
    page.get_by_label("Last Name:").fill("Borade")
    page.get_by_label("EMail:").fill("abc@gmail.com") 
    page.wait_for_timeout(5000)
    
    # 5) page.get_by_placeholder()
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.get_by_placeholder("Search store").fill("Apple MacB0ook Pro")
    page.wait_for_timeout(5000)
    page.wait_for_load_state("networkidle")
    page.close()
    
    # 6) page.get_by_title()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(5000)

    # 7) page.get_by_test_id()
    
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
    page.wait_for_timeout(5000)
    page.close()