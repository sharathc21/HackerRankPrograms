class Solution:
    def isValid(self, s: str) -> bool:
        map1 = {")": "(", "]": "[", "}": "{"}
        stack1 = []

        for c in s:
            if c not in map1:
                stack1.append(c)
                continue
            if stack1 and stack1[-1] != map1[c]:
                return False
            stack1.pop()

        return not stack1

print(Solution().isValid("()["))
