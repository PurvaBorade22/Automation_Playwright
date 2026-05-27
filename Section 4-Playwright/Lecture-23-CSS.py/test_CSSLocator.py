
# tag id          tag#id
# tag class       tag.class
# tag attribute   tag[attribute=value]
# tag class attribute     tag.class[attribute=value]

from playwright.sync_api import Page, expect

def test_verify_css_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    
    # # 1) tag id - tag#id
    # page.locator("#small-searchterms").fill("T-shirt")
    # page.wait_for_timeout(5000)
    
    # 2) tag class - tag.class
    page.locator("input.search-box-text").fill("T-shirt")
    page.wait_for_timeout(5000)  