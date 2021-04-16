import pytest


@pytest.mark.usefixtures("setup")
class TestExample:


    def test_Demofixturesecondmethod(self):
         print("second will be executed after fixture executed")

    def test_Demofixturefirstmethod(self):
         print("frst will be executed after fixture executed")

    def test_Demofixturethirdmethod(self):
        print("Third will be executed after fixture executed")