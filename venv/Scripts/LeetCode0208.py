class Solution(object):
    def minOperations(self, s) -> int:
        self.s = s
        zerobegin = 0
        onebegin = 0
        for i in range(len(self.s)):
            if i % 2:
                if self.s[i] == '1':
                    zerobegin += 1

                else:
                    onebegin += 1

            else:
                if self.s[i] == '1':
                    onebegin += 1
                else:
                    zerobegin += 1
        return min(onebegin, zerobegin)

obj = Solution()
print(obj.minOperations("10"))
