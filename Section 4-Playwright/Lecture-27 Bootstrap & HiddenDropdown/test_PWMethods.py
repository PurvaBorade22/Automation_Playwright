import pytest

from playwright.sync_api import Page, expect

def test_comparisonosmethods(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    
    products = page.locator(".product-title")
    
    # # 1) inner_text() vs test_content()
    # print("Using inner_test()==>",products.nth(1).inner_text())  # return actual text
    # print("Using text_content()==>",products.nth(1).text_content()) # returns content with special chars and spaces

    #print content of all the products
    #step1 - count
    count = products.count()
    
    #step2- print using for loop
    # for i in range(count):
    #     product_names= products.nth(i).text_content() 
    #     print(product_names.strip())
    #     # product_names= products.nth(i).inner_text()
    #     # print(product_names)
        
    # 2) all_inner_text() vs all_text_content()
    # product_names= products.all_inner_texts()
    # product_names = products.all_text_contents()
    # print(product_names)
    # productnames_trimmed = [text.strip() for text in product_names]
    # print(productnames_trimmed)
    
    #3) all() method
    product_locator = products.all()
    
    for product_loc in product_locator:
        print(product_loc.inner_text())
    
        
    page.wait_for_timeout(5000)