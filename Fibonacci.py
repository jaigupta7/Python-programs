n = int(input("Enter the number of Fibonacci numbers to generate: "))
a, b = 0, 1
print(a, end=" ")
for _ in range(1, n):
    print(b, end=" ")
    a, b = b, a + b
