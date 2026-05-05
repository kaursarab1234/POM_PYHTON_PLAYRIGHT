import pytest

def test_firstmethod():
    print("test_file2_method")

@pytest.mark.smoke 
@pytest.mark.order(1) 
def test_firstmethod1():
    print("test_file2_method1")

def test_firstmethod2():
    print("test_file2_method2")

def test_firstmethod3():
    print("test_file2_method3")
@pytest.mark.skip
def test_firstmethod4():
    print("test_file2_method4")