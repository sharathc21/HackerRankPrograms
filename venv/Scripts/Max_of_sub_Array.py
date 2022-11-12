class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
           # initialize max_sum with the lowest possible value and cur_sum for comparison
        max_sum, cur_sum = float('-inf'), 0
        print(type(max_sum), type(cur_sum))
        print(max_sum, cur_sum)

        for n in nums:
            cur_sum = max(cur_sum+n, n)
            print('for n value', n, 'Current is', cur_sum)
            max_sum = max(max_sum, cur_sum)
            print('max', max_sum, ', cur', cur_sum)

        return max_sum

lst= [-2,1,-3,4,-1,-2,1,-5,4]
a= Solution()
print('\nmaximum sum of sub array is', a.maxSubArray(lst))