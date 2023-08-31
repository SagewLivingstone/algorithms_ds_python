
"""
Simple binary search
"""
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = int((low + high) / 2)
        guess = arr[mid]

        if (guess == key):
            return mid
        elif (guess < key):
            low = mid + 1
        else:
            high = mid - 1

"""
Binary search - recursive version
"""
def bin_search(arr, key, low=0, high=None):
    if high is None: 
        high = len(arr)-1

    mid = int((low + high) / 2)
    guess = arr[mid]

    if (guess == key): return mid
    elif (guess < key): return bin_search(arr, key, mid+1, high)
    else: return bin_search(arr, key, low, mid-1)

if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(11):
        print(i, bin_search(arr, i))