def factorial(x):
# Method which computes factorial of a given number using recursion
    if(x == 0):
        return 1
    return x * factorial(x - 1)

print(factorial(int(8)))