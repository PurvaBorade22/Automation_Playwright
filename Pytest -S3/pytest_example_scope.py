import pytest

# scope="function"  fixture will be called before every test function executes
# scope="module"   fixture will be called only once before test functions executes
# scope="class"   fixture will be called only once before the class
# scope="session"  fixture will be called only once for session


@pytest.fixture
def setup(scope= "class"):
    print("setup browser")           

def test_one(setup):
    print("This is test one")
    
def test_two(setup):
    print("This is test two")

def test_three(setup):
    print("This is test three")