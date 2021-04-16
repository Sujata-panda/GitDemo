import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("user profile data created")
    return ["sujtaa", "panda", "QA"]

@pytest.fixture(params=[("chrome", "sujata"),("Firefox", "panda"), ("IE","qa")])
def CrossBrowser(request):
    return request.param
