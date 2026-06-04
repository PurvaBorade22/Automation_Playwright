import pytest

from playwright.sync_api import Page, expect

def test_bootstrap_Dropdown(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    page.locator('input[name="username"]').fill("Admin")
    page.locator('input[name="password"]').fill("admin123")
    page.locator('button[type="submit"]').click()
    
    page.wait_for_timeout(3000)
    
    #click on PIM
    page.get_by_text('PIM').click()
    
    # click on job title dropdown
    page.locator('Form i').nth(2).click()
    page.wait_for_timeout(4000)
    
    #capture all the options from the dropdown
    options = page.locator("div[role='option'] span")
    
    count = options.count()
    print("The total no. os dropdwon options are:",count)
    
    page.wait_for_timeout(5000)
    
    expect(options).to_have_count(count)
    
    print("All the options:",options.all_text_contents())
    
    for i in range(count):
        print(options.nth(i).text_content())
        
        
    #selecting a option from a dropdown
    for i in range(count):
        text=options.nth(i).inner_text()
        if text=='Finance Manager':
            print("matching success")
            options.nth(i).click()
            break    
    
    page.wait_for_timeout(5000)