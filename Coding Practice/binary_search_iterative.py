data = [2, 4, 6, 8, 10, 13, 15, 16, 17, 18, 20, 22, 23, 25, 26, 28, 30]
target = 19


# Binary Search Iterative
def binary_search_iterative(data, target):
    low = 0
    high = len(data)

    while low <= high:
        mid = (high + low) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Binary Search Recursive
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)))