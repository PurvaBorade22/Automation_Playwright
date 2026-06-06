import pytest
from playwright.sync_api import Page, expect

def test_flipkart_website(page:Page):
    #1) 
    page.goto("https://www.flipkart.com/")
    
    #2)
    search_box= page.locator("input[name='q']:not([readonly])")
    search_box.fill("smart")
    
    page.wait_for_timeout(3000)
      
    #3)Step 3: Locate all suggestions
    options = page.locator("ul > li")
    count = options.count()
    print("Options are:",count)
    
    # printing 5th suggestion
    if count > 5:
        print("5th option",options.nth(5).inner_text())
        
    # all suggestion print
    for i in range(count):
        print(options.nth(i).all_inner_texts())
    
    # clicking on one option
    for i in range(count):
        text = options.nth(i).inner_text()
        if text.strip().lower() == "smartphone":
            options.nth(i).click
            break
    
    
    page.wait_for_timeout(5000)
    
   
    