class Solution(object):
    def palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n1 = x
        n2 = x
        n3 = 0

        while (0 < n2):
            n3 = n3 * 10 + (n2 % 10)
            n2 = n2 // 10

        if (n1 == n3):
            print("true")
        else:
            print("false")




nums= 121

Solution().palindrome(nums)
