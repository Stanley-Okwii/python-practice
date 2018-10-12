def divideByZero():
    return 5/0

try:
    divideByZero()
except ZeroDivisionError:
    print("Attempt to divide by zero")
except Exception:
    print("Caught an exception")
finally:
    print("Block code for clean up")
