# Define a function named factorial that takes an integer n as its parameter.
# Inside the function, implement the factorial calculation using a loop.
# The function should return the factorial of the input number n.
# Outside the function, prompt the user to enter an integer and store it in a variable.
# Call the factorial function with the user's input as an argument and store the result in a variable.
# Print the factorial of the input number.
# Example Output:
# Enter an integer: 5
# The factorial of 5 is 120.
# Note: The factorial of a non-negative integer n,
# denoted as n!, is the product of all positive integers less than or equal to n.
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    # Get factorial of n using loop
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return (fact)


factorial_input = int(input('Please enter number to calculate the factorial\n'))
print(factorial(factorial_input))
