p = [2, 8, 10, 12, 16, 18, 20, 25]
r = [None] * len(p)


def max_price(cur_len):
    if cur_len == 1:
        r[0] = p[0]
        return r[0]
    else:
        cur_max = p[cur_len - 1]
        for i in range(cur_len - 1):
            new_len = cur_len - (i + 1)
            if r[new_len - 1] is None:
                cur_max = max(cur_max, p[i] + max_price(new_len))
            else:
                cur_max = max(cur_max, p[i] + r[new_len - 1])
        r[cur_len - 1] = cur_max
        return cur_max


print(max_price(8))
print(p)
print(r)
