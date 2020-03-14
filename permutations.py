def permutate(s):
    res = set()
    if len(s) <= 1:
        res.add(s)
    else:
        for c in s:
            tmp = s
            for p in permutate(tmp.replace(c,'',1)):
                res.add(c+p)
    return res


print(permutate('ABC'))
