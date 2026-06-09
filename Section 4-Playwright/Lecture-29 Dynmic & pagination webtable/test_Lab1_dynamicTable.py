import pytest
import re
from playwright.sync_api import Page,expect

def test_Excercise_dynamic_table(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    table = page.locator("#taskTable tbody")

    #get all the rows
    rows = table.locator("tr").all()

    # 1) chrome
    cpu_load = ""
    for row in rows:
        process_chrome=row.locator("td").nth(0).inner_text()
        if process_chrome == "Chrome":
            cpu_load = row.locator("td",has_text="%").inner_text()
            print("CPU load is:-",cpu_load)
            break

    expect(page.locator(".chrome-cpu")).to_contain_text(cpu_load)

    #2) senario = 2 firfox
    memory_size=""
    for row in rows:
        process_firefox = row.locator("td").nth(0).inner_text()
        if process_firefox == "Firefox":
            memory_size = row.locator("td",has_text=re.compile("MB$")).inner_text()
            print("Memory size of firefox:-",memory_size)
            break 

    expect(page.locator(".firefox-memory")).to_contain_text(memory_size)

    # 3) Scenario -3 network speed
    network_speed=""
    for row in rows:
        process_network = row.locator("td").nth(0).inner_text()
        if process_network == "Chrome":
            network_speed = row.locator("td",has_text=re.compile("Mbps$")).inner_text()
            print("Chrome network speed:",network_speed)
            break

    expect(page.locator(".chrome-network")).to_contain_text(network_speed)


    # 4) Scenario -4 Disk Speace
    disk_space=""
    for row in rows:
        process_disk = row.locator("td").nth(0).inner_text()
        if process_disk=="Firefox":
            disk_space = row.locator("td",has_text=re.compile("MB/s$")).inner_text()
            print("firefox disk space:",disk_space)
            break
        
    expect(page.locator(".firefox-disk")).to_contain_text(disk_space)
    page.wait_for_timeout(5000)