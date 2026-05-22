import pytest

def test_login_by_phone():
    print("Login by phone")
    assert 1 == 1
    
@pytest.mark.skip
def test_login_by_email():
    print("Login by email")
    assert 1 == 1
    
def test_login_by_facebook():
    print("Login by facebook")
    assert 1 == 1

@pytest.mark.skip
def test_signup_by_email():
    print("Signup by email")
    assert 1 == 1
    
@pytest.mark.skip
def test_signup_by_facebook():
    print("Signup by facebook")
    assert 1 == 1

def test_signup_by_google():
    print("Signup by google")
    assert 1 == 1
    