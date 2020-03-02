def match(p, t):
    if not bool(p):
        return not bool(t)
    ans = bool(t) and p[0] in [t[0], '.']
    return ans and match(p[1:], t[1:])

print(match('m.ss.ssi..', 'mississipi'))
