#!/usr/bin/env python3
def print_fibonacci(length):
    fib_sequence = []  # Initialize an empty list to store the Fibonacci sequence

    if length >= 1:
        fib_sequence.append(0)  # Add the first Fibonacci number

    if length >= 2:
        fib_sequence.append(1)  # Add the second Fibonacci number

    # Generate Fibonacci sequence up to the specified length
    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    # Print the Fibonacci sequence
    print(fib_sequence)

    # Return the Fibonacci sequence as a list
    return fib_sequence

print_fibonacci(9)
