# PYTEST rule::::::::::::::
# python package name should be start with test_ or end with test_
# all code should be written inside function
# pytest method name should be start with test keyword
# run code in pytest in 2 ways (cmd format or test runner)
# run(right top project name->edit configuration-plus icon>python test->pytest->give file path->apply->run in up
# in pytest every method treated as one test case
# in pytest same method name not possible in a file
import pytest


@pytest.mark.smoke
def test_firstmethod():
    print("sujata")

@pytest.mark.skip
def test_secondmethod():
    print("panda")


def test_crossBrowser(CrossBrowser):
    print(CrossBrowser)


