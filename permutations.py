def permutate(s):
    res = []
    if len(s) <= 1:
        res.append(s)
    else:
        for i in range(len(s)):
            for p in permutate(s[:i] + s[i+1:]):
                res.append(s[i]+p)
    return res

print(permutate('(())'))
