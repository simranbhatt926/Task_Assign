def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

# Prompt the user to enter the number of terms
n = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence and display it
fibonacci_sequence = generate_fibonacci(n)
print(fibonacci_sequence)
