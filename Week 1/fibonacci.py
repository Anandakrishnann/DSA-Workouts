def fibonacci(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1

    else:
        print(fibonacci(n - 1) + fibonacci(n - 2),end="-->")
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  


def custom_fibonacci(n, a, b):

    if n == 0:
        return a
    elif n == 1:
        return b

    else:
        return custom_fibonacci(n - 1, a, b) + custom_fibonacci(n - 2, a, b)

a = 3  
b = 5  
print(custom_fibonacci(5, a, b)) 