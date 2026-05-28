from playwright.sync_api import Page,expect

def test_verify_css_locator(page:Page):
    # 1) launch website
    page.goto("https://demowebshop.tricentis.com/")
    
    #2)logo (CSS locator)
    Logo = page.locator('img[alt="Tricentis Demo Web Shop"]')
    expect(Logo).to_be_visible()
    
    #3)Products containing "computer" in href attribute
    products= page.locator('h2>a[href*="computer"]')
    print("Products count is:",products.count())
    expect(products).to_have_count(4)
    
    print("first computer name:",products.first.text_content())
    print("last product name:",products.last.text_content())
    print("nth product name:",products.nth(3).text_content())
    
    # all product title
    product_title = products.all_text_contents()
    print("All computer text contents:",product_title)
    
    # for pt in product_title:
    #     print(pt)

    # links 
    register_link = page.locator('a[href="/register"]')
    expect(register_link).to_be_visible()
    
    # social media link last
    google_plus = page.locator('.follow-us ul li:last-child')
    expect(google_plus).to_have_text("Google+")
    
    # second social media link
    twitter_link = page.locator("a[href='https://twitter.com/nopCommerce']")
    expect(twitter_link).to_have_text("Twitter")
    
    
