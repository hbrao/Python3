import numpy as np


def longest_common_sub_str(s1, s2):
    """Returns the longest common substring"""
    res = 0
    res_idx = 0
    mx = np.zeros((len(s1) + 1, len(s2) + 1))
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i > 0 and j > 0:
                x = s1[i-1]
                y = s2[j-1]
                if x == y:
                    mx[i][j] += mx[i-1][j-1] + 1
                    if mx[i][j] > res:
                        res = mx[i][j]
                        res_idx = i
    if res > 0:
        return s1[(int(res_idx) - int(res)):int(res_idx)]
    else:
        return None


str1 = "ABCDEFG"
str2 = "HICDEJ"
print(longest_common_sub_str(str1, str2))
