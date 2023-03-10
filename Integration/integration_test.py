# import addition
# import multiplication
#
# def test_integration():
#     # Test multiplying the result of adding two numbers with another number
#     assert multiplication.multiply(addition.add(2, 3), 4) == 20

import calculator
import input_handler
import requests

def test_addition():
    assert calculator.add(2, 3) == 5

def test_subtraction():
    assert calculator.subtract(5, 3) == 2

def test_multiplication():
    assert calculator.multiply(2, 3) == 6

def test_division():
    assert calculator.divide(6, 3) == 2

def test_divide_by_zero():
    try:
        calculator.divide(6, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Expected ValueError"

# def test_input_handler():
#     # Test get_num_input()
#     input_handler.input = lambda _: "3.14"
#     assert input_handler.get_num_input() == 3.14
#
#     # Test get_op_input()
#     input_handler.input = lambda _: "+"
#     assert input_handler.get_op_input() == "+"

# def test_input_handler():
#     # # Test valid operator input
#     # assert input_handler.get_op_input("Enter an operator (+, -, *, /): ") == "+"
#     # assert input_handler.get_op_input("Enter an operator (+, -, *, /): ") == "-"
#     # assert input_handler.get_op_input("Enter an operator (+, -, *, /): ") == "*"
# #     assert input_handler.get_op_input("Enter an operator (+, -, *, /): ") == "/"
# #
#     # Test invalid operator input
#     input_values = ["%", "abc", "", "(", ")", "1"]
#     expected_output = ["Invalid input. Please enter an operator (+, -, *, /): "] * len(input_values)
#     for i in range(len(input_values)):
#         with mock.patch('builtins.input', return_value=input_values[i]):
#             assert input_handler.get_op_input("Enter an operator (+, -, *, /): ") == expected_output[i]

