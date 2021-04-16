import pytest

from PytestDemo.Baselog import Baseclass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(Baseclass):


    def test_editProfile(self, dataLoad):
            log=self.getlogger()
            log.info(dataLoad)
            log.info(dataLoad[0])
           # print(dataLoad)
           # print(dataLoad[0])