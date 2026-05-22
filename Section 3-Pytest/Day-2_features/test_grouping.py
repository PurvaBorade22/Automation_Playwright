import pytest

# grouping tests:
# --------------
# test_LoginByEmail -> sanity , regression
# test_LoginByFacebook -> sanity
# test_LoginByPhone -> regression
# test_signupByEmail -> sanity, regression
# test_signupByFacebook -> regression
# test_signupbyphone -> sanity
# test_paymentindollor -> sanity, regression
# test_paymentinrupees -> regression

@pytest.mark.regression
@pytest.mark.sanity
def test_login_by_phone():
    print("Login by phone")
    assert 1 == 1
    
@pytest.mark.regression
@pytest.mark.sanity
def test_login_by_email():
    print("Login by email")
    assert 1 == 1
    
    
@pytest.mark.sanity
def test_login_by_facebook():
    print("Login by facebook")
    assert 1 == 1

@pytest.mark.regression
@pytest.mark.sanity
def test_signup_by_email():
    print("Signup by email")
    assert 1 == 1
    
@pytest.mark.regression
def test_signup_by_facebook():
    print("Signup by facebook")
    assert 1 == 1

@pytest.mark.sanity
def test_signup_by_google():
    print("Signup by google")
    assert 1 == 1
    