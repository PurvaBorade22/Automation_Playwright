import pytest


@pytest.fixture
def setup(scope= "class"):
    print("setup browser")
    return "Chrome"           #return value

def test_one(setup):
    print("This is test one")
    print("The browser is", setup) #print the return value of fixture
    
def test_two(setup):
    print("This is test two")
    print("The browser is", setup) #print the return value of fixture

def test_three(setup):
    print("This is test three")
    print("The browser is", setup) #print the return value of fixture