n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Sequence:")
print(a, b, end=" ")
for _ in range(n - 2):  
    c = a + b
    print(c, end=" ")
    a, b = b, c
