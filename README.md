Fibonacci Number Calculator

This Python project calculates Fibonacci numbers up to a desired value.

How to use:

Clone the repository:

Bash
git clone https://github.com/abhiraj081006/FibonacciSeries.git

Run the script:

Bash
python Fibonacci.py

Enter the desired value:
The script will prompt you to enter the value up to which you want to calculate Fibonacci numbers.

View the results:
The script will print the Fibonacci numbers up to the entered value.

Example:

If you enter 10, the script will print:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34
Code:

Python
# Define a function to find the Fibonacci series up to n times
def fibonacci(n):
  # Initialize the first two numbers of the series
  a = 1
  b = 1
  # Print the first two numbers
  print(a)
  print(b)
  # Loop from the third term to the nth term
  for i in range(3, n + 1):
    # Calculate the next number as the sum of the previous two numbers
    c = a + b
    # Print the next number
    print(c)
    # Update the previous two numbers
    a = b
    b = c

# Ask the user to enter a positive integer
n = int(input("Enter a positive integer: "))

# Find and print the Fibonacci series up to n times
fibonacci(n)

Use code with caution.

License:

This project is licensed under the GNU GENERAL PUBLIC LICENSE.
