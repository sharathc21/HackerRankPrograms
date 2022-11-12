class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tcount = {}
        slide = {}
        for c in t:
            tcount[c] = 1 + tcount.get(c, 0)

        have = 0
        need = len(t)
        res = [-1, -1]
        reslen = float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            slide[c] = 1 + slide.get(c, 0)
            if c in tcount and slide[c] >=tcount[c]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = (r - 1 + 1)

                slide[s[l]] -= 1
                if s[l] in tcount and slide[s[l]] < tcount[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l-1:r + 1] if reslen != float("infinity") else ""


s= "ab"
t= "b"
print(Solution().minWindow(s, t))
