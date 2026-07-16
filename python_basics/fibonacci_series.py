# fibonacci_series.py
# Print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
