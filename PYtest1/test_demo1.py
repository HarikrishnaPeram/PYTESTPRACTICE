import pytest


def test_FirstProgram():
    print("Hello")
def test_SecondProgram():
    print("World")
@pytest.mark.usefixtures("crossBrowser")
def test_crossbrowser():
    print("Iam executing all browser")