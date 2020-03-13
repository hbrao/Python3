def permutate(s):
    res = []
    if len(s) <= 1:
        res.append(s)
    else:
        for c in s:
            tmp = s
            for p in permutate(tmp.replace(c,'')):
                res.append(c+p)
    return res


print(permutate('ABC'))
