
#Print the Fibonacci series up to n terms.
#In Fibonacci, each number is the sum of the two before it:

def fibonacci_series(n):
    a = 1
    b = 2
    print(a, b, end=" ")

    for _ in range(n - 2):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

fibonacci_series(7)

