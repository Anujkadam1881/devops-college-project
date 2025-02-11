import math

def factorial_of_two_numbers(num1, num2):
    factorial_num1 = math.factorial(num1)
    factorial_num2 = math.factorial(num2)
    return factorial_num1, factorial_num2

# Example usage
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

factorial1, factorial2 = factorial_of_two_numbers(number1, number2)

print(f"The factorial of {number1} is {factorial1}")
print(f"The factorial of {number2} is {factorial2}")
