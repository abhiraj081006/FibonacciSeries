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
