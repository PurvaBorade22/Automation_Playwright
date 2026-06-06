import pytest

from playwright.sync_api import Page,expect

def test_static_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()
    
    #counting the rows in the tbale
    rows = table.locator("tr")     # equals to table[name='BookTable'] tbody tr
    expect(rows).to_have_count(7)
    
    rows_count = rows.count()
    print("rows count are:",rows_count)
    
    #counting columns of the table
    columns= rows.locator("th")  # equals to quals to table[name='BookTable'] tbody tr th
    expect(columns).to_have_count(4)
    
    columns_count = columns.count()
    print("Colunms count is:",columns_count)
    
    page.wait_for_timeout(4000)

    # reading data from second row
    second_row = rows.nth(2).locator("td")
    second_row_text = second_row.all_inner_texts()
    print("2nd row text:-",second_row_text)
    
    #printing data one by one
    for text in second_row_text:
        print(text)
        
    #printing all the rows and column data
    all_rows_data = rows.all()
    
    # print("Rows and coloumn data")
    # for row in all_rows_data[1:]:
    #     cols= row.locator('td').all_inner_texts()
    #     print(cols)
    
    # 5. Print Book names whose author is 'Mukesh'
    for row in all_rows_data[1:]:
        author_name = row.locator('td').nth(1).inner_text()
        if author_name == 'Mukesh':
            book_name = row.locator('td').nth(0).inner_text()
            print(f"{author_name} \t {book_name}")
        
    #6. Calculate total price of all the books
    total_price = 0
    for row in all_rows_data[1:]:
        price = row.locator('td').nth(3).inner_text()
        total_price += int(price)
        print("Total price:", total_price)