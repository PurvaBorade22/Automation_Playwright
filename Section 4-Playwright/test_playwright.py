from playwright.sync_api import Page ,expect

def test_verifyPageUrl(page:Page):
    page.goto("https://demowebshop.tricentis.com/") #passing url to the page
    
    myurl =page.url                     #property
    print("my url is:", myurl)
    
    expect(page).to_have_url("https://demowebshop.tricentis.com/") #expected url 
    
def test_verifyTitle(page:Page):
    page.goto("https://demowebshop.tricentis.com/") #passing url to the page
    
    mytitle = page.title()               #method
    print("My title is:", mytitle)
    
    expect(page).to_have_title("Demo Web Shop") #expected title of the page