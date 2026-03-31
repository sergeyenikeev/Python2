import pytest
from calc import Calculator
#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
#setUp method is overridden from the parent class TestCase
# def setUp(self):
#     self.calculator = Calculator()
# #Each test method starts with the keyword test_
# def test_add(self):
#     assertEqual(self.calculator.add(4,7), 11)
# def test_subtract(self):
#     assertEqual(self.calculator.subtract(10,5), 5)
# def test_multiply(self):
#     assertEqual(self.calculator.multiply(3,7), 21)
# def test_divide(self):
#     assertEqual(self.calculator.divide(10,2), 5)
# # Executing the tests in the above test case class
# if __name__ == "__main__":
#   unittest.main()


def test_add():
    assert 11 == 11

def test_add2():
    assert 12 == 11
