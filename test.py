import pytest
from app import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2,3) == 5
    assert calculator.add(-1,1) == 0
    assert calculator.add(0,0) == 0
    assert calculator.add(-5,-7) == -12