import random


def binary_search(sl, low, high, val):
    if low == high:
        if val == sl[low]:
            return low
        else:
            return None
    elif low < high:
        mid = (low + high) // 2
        if val > sl[mid]:
            return binary_search(sl, mid + 1, high, val)
        elif val < sl[mid]:
            return binary_search(sl, low, mid - 1, val)
        else:
            return mid
    else:
        return None


def nr_binary_search(sl, val):
    low = 0
    high = len(sl) - 1
    while low <= high:
        mid = (low + high) // 2
        if val > sl[mid]:
            low = mid + 1
        elif val < sl[mid]:
            high = mid - 1
        else:
            return mid
    return - (low)


data = [random.randint(0, 10) for i in range(10)]
data.sort()
val = random.randint(0, 10)

idx = binary_search(data, 0, len(data) - 1, val)
print("Found {} at index {} in {}".format(val, idx, data))

jdx = nr_binary_search(data, val)
print("Found {} at index {} in {}".format(val, jdx, data))
