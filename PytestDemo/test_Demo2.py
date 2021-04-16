import pytest


def test_firstmethod():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string do not match"

@pytest.mark.xfail
def test_secondmethod():
    a = 2
    b = 4
    assert a+b == 6, "addition not match"
