class Solution:
    def isMatch(self, t: str, p: str) -> bool:
        if not p:
            return not t
        ans = bool(t) and p[0] in [t[0], '.']
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(t, p[2:]) or (ans and self.isMatch(t[1:], p))
        else:
            return ans and self.isMatch(t[1:], p[1:])

print(Solution().isMatch('mississipi', 'm.s*is*i.*'))