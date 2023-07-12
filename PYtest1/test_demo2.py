import pytest as pytest

from PYtest1.conftest import setup

@pytest.mark.usefixtures("setup")
class TestExample:
    @pytest.mark.xfail
    def test_firstprogram(self):
        meg = "Hello"
        assert meg =="Hi" "This string got failed because not matched"

    def test_fourthprogram(self):
         a= 2
         b=8
         assert a+b==10, "Addition does not match"
    def test_fifthprogram(self):
        print("Iam 5th program")

    def test_sixthprogram(self):
        print("iam 6th program")