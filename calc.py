import random

"""
Recursive sum
"""
def sum(arr):
    if arr == []: return 0
    return arr[0] + sum(arr[1:])

"""
Recursive count
"""
def count(arr):
    if arr == []: return 0
    return 1 + count(arr[1:])

"""
Recursive max of array
"""
def max(arr):
    if len(arr) == 1: return arr[0]
    m = max(arr[1:])
    return arr[0] if arr[0] > m else m

"""
Calculates the factorial of x, x!
"""
def factorial(x):
    if (x <= 1):
        return x
    else:
        return x * factorial(x-1)

if __name__ == "__main__":
    for f in range(10):
        print(f'Factorial of {f} = {factorial(f)}')