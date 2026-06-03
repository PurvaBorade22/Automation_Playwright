import pytest
from playwright.sync_api import Page, expect

def test_productpage(page:Page):
    #1)
    page.goto("https://www.bstackdemo.com/")
    
    # 2)
    orderby_dropdown = page.locator("div.sort>select")
    expect(orderby_dropdown).to_be_visible()
    expect(orderby_dropdown).to_be_enabled()
    
    #3) 
    page.locator("div.sort>select").select_option(value="lowestprice")
    
    # 4)
    product_names= page.locator(".shelf-item__title")
    price_list = page.locator(".val")
    
    product_text = [text.strip() for text in product_names.all_text_contents()]
    print("Priduct names are:",product_text)
    
    price_text = [price.strip() for price in price_list.all_text_contents()]
    print("All prices are:",price_text)
    
    # 5)
    print("Product names alone with the price")
    for i in range(len(product_text)):
        print(f"{product_text[i]}: {price_text[i]}")
        
    # 6) lowest and highest product
    print(f"Lowest priced product:{product_text[0]}:{price_text[0]}")
    print(f"Highest priced product:{product_text[-1]}:{price_text[-1]}")
    
    
    page.wait_for_timeout(9000)