import time

from playwright.sync_api import Page , expect

def test_login_page(page:Page):
    
    #1) page to go
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # 2) verigy logo
    logo = page.get_by_alt_text("company-branding")
    expect(logo).to_be_visible()
    
    # 3) Login
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    
    # 4) login button
    page.get_by_role("button", name = "Login").click()
    # page.wait_for_timeout(5000)
    
    # 2) heading
    expect(page.get_by_role("heading", name = "Dashboard")).to_be_visible()
    # page.wait_for_timeout(5000)
    page.close()