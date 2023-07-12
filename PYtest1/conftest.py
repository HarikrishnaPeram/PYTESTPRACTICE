import pytest


@pytest.fixture(scope ="class")
def setup():
    print("I will execute first")
    yield
    print("I will Execute last")

@pytest.fixture()
def dataload():
    print("user profile data created")
    return ["Hari","Krishna","peram.harikrishna@gmail.com"]

@pytest.fixture(params=["chrome", "Firefox","IE"])
def crossBrowser(request):
    return request.param



