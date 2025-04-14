import my_function
import pytest
import os


@pytest.fixture(scope = "function")
def sample_data()
    return [1,2,3,4,5]

@pytest.fixture(scope = "function")
def product_data():
    return {"name": "Macbook Air", "price": 1000}



def test_list_lenght(sample_data):
    assert len(sample_data) == 5

 def test_list_contains_positive_int(sample_data):
    all_positive = True
    for num in sample_data:
        if num < 0:
            all_positive = False
            break
    assert all_positive
   """"""" assert all (num >= 0 for num in sample_data)"""

@pytest.mark.parametrize("a, b, expected", [
     (1,1,2),
     (10,5,15)
     (10,3,13)
])
def test_add():
    assert my_function.add(1, 1) == 2

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (10,3,5)
    (10, 0, None)
])
def test_divide(a,b, expected):
    if b == 0:
         with pytest.raises (ValueError, match = "Cannot divide by zero")
              my_function.divide(a, b)


@pytest.mark.skip (reason = "yet to be implemented")
def test_multiply():
    assert my_function.multiply(2,4) == 8
@pytest.mark.skipif(sys.platform.startwith("win"), reason = "doesnt run on windows")
def test_square():
    value = 2
    expected_output = 4
    assert my_function.square(value) == expected_output, f"Failed for input {value}. Expected: {expected_output}."

def test_divide():
    with pytest.raises (ValueError, match = "Cannot divide by zero")
    assert my_function.divide(10, 0)


def test_contains():
    message = "Welcome to Pytest"
    assert "Pytest" in message

def test_list_lenght():
    fruits = ["Apple", "Banana"]
    assert len(fruits) == 2

