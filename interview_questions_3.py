# Import the math module to access mathematical functions
import math

def compute_factorial(number):
    # Compute the factorial of "number" using Python's built-in factorial function from the math module.
    return math.factorial(number)


# Test. Verification of compute_factorial function
def test_compute_factorial():
    # Define the input number
    input_number = 5

    # Perform the factorial computation
    result = compute_factorial(input_number)

    # Check if the result is equal to the expected factorial value
    assert result == 120

    print("Test Passed! The factorial of " + str(input_number) + " is " + str(result))