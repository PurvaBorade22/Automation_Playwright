import pytest



@pytest.fixture
def setup():
    print("setup browser") 
    yield 
    print("Close browser")           #teardown code after yield statement

def test_one(setup):
    print("This is test one")
    
def test_two(setup):
    print("This is test two")

def test_three(setup):
    print("This is test three")