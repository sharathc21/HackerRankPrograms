class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                print(nums.index(remaining))
                return [i, seen[remaining]]


            seen[value] = i

nums = [2,7,11,15]
target = 9
Solution().twoSum(nums, target)