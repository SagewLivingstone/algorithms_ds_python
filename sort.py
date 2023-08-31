import math
import random

"""
Finds the max value in a given array
"""
def find_max(arr):
    max = -math.inf
    for item in arr:
        if item > max:
            max = item
    return max

"""
Selection sort
---
O(n^2)
"""
def selection_sort(arr):
    result = []
    for _ in range(len(arr)):
        max = find_max(arr)
        result.append(max)
        arr.remove(max)
    return result


"""
Quicksort
"""
def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivi = random.randint(0, len(arr)-1)
    pivot = arr[pivi]
    remaining = arr[0:pivi] + arr[pivi+1:]
    less = [x for x in remaining if x <= pivot]
    more = [x for x in remaining if x > pivot]
    return quicksort(less) + [pivot] + quicksort(more)


if __name__ == "__main__":
    arr = [random.randint(-100, 100) for _ in range(20)]

    print(arr)
    print(quicksort(arr))