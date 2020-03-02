def match(p, t):
    if not bool(p):
        return not bool(t)
    ans = bool(t) and p[0] in [t[0], '.']
    if len(p) > 1 and  p[1] == '*':
        return ans and ( match(p, t[1:]) or match(p[2:], t[1:]) )
    else:
        return ans and match(p[1:], t[1:])

print(match('m.ss.ssi..', 'mississipi'))
print(match('m.s*.s*i.*', 'mississipi'))
