import pytest
from playwright.sync_api import Page,expect

def test_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    
    # 1) Absoulate xpath
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()
    
    # 2) Relative xpath
    logo = page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()
    page.wait_for_timeout(5000)
    
    # 3) xpath with contain
    products= page.locator("//h2//a[contains(@href,'computer')]")
    products_count= products.count()
    print("Products count:",products_count)
    expect(products).to_have_count(products_count)
    
    # 4) product first,last, and nth name
    print("Product first name is:",products.first.text_content())
    print("Products last name is:",products.last.text_content())
    print("Product nth name is:",products.nth(3).text_content())
    
    product_titles = products.all_text_contents()
    print("All the products contain are:", product_titles)
    
    for i in product_titles:
        print(i)
    
    #5) xpath witn text - - is representing inner text of the element
    registration_link = page.locator("//a[text()='Register']")
    expect(registration_link).to_be_visible()
    
    # 6) xpath with last or first keywords
    google_link=page.locator("//div[@class='column follow-us']//li[last()]")
    expect(google_link).to_have_text("Google+")

    # 7) xpath with position()
    twiter_link =page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twiter_link).to_have_text("Twitter")  
    

