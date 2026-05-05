import pytest
@pytest.fixture(scope="session")
def precondition():
    print("i am in precondition ")

def test_firstmethod():
    l1=[1,2]
    print("test_file1_method")
    print(l1[2])

@pytest.mark.smoke 
@pytest.mark.regressionp
def test_firstmethod1(precondition):
    print("test_file1_method1")

def test_firstmethod2():
    print("test_file1_method2")

def test_firstmethod3():
    print("test_file1_method3")

def test_firstmethod4():
    print("test_file1_method4")