import pytest

@pytest.fixture()
def setup():
    print("Environment setup...")
    yield
    print("Environment teardown...")