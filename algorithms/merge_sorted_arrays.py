import random


def merge_sorted_arrays(nums1, nums2):
    """Merges two sorted array and returns the merged array"""
    out = []
    size = len(nums1) + len(nums2)
    p = q = 0
    for i in range(size):
        if q >= len(nums2) \
                or (p < len(nums1) and nums1[p] < nums2[q]):
            out.append(nums1[p])
            p += 1
        else:
            out.append(nums2[q])
            q += 1
    return out


l1 = [random.randint(10, 99) for i in range(10)]
l2 = [random.randint(10, 99) for i in range(10)]
l1.sort()
l2.sort()
print(l1)
print(l2)
print(merge_sorted_arrays(l1, l2))
