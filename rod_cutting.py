p = [2, 8, 10, 12, 16, 18, 20, 25]

def max_price(n):
    if n == 0:
        return p[0]
    else:
        cur_max = p[n-1]
        for i in range(n):
            cur_max = max(cur_max, p[i] + max_price(n-i-1))
        return cur_max

print(max_price(5))