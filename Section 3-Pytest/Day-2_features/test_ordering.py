# import pytest 

# def test_login():
#     print("Login in successfully")
    
# def test_add_item():
#     print("Product added to cart successfully")
    
# def test_logout():
#     print("Logout successfully")
    
    
# Approach 1: order tests by position

# import pytest 

# @pytest.mark.order(2)
# def test_add_item():
#     print("Product added to cart successfully") 
    
# @pytest.mark.order(3)
# def test_logout():
#     print("Logout successfully")
    
# @pytest.mark.order(1)
# def test_login():
#     print("Login in successfully")


# Approach 2: using before , after

# import pytest 

# @pytest.mark.order(before = "test_logout")
# def test_add_item():
#     print("Product added to cart successfully") 
    
# @pytest.mark.order(after = "test_add_item")
# def test_logout():
#     print("Logout successfully")
    
# @pytest.mark.order(1)
# def test_login():
#     print("Login in successfully")
    
# Approach 3: using marker string ( user defined)

import pytest 

@pytest.mark.order()
def test_add_item():
    print("Product added to cart successfully") 
    
@pytest.mark.order("last")
def test_logout():
    print("Logout successfully")
    
@pytest.mark.order("first")
def test_login():
    print("Login in successfully")