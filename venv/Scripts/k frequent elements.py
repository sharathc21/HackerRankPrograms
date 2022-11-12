from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # self.nums = nums
        # self.k = k
        #         length = len(nums) # total number of values in the array

        # 		# frequency_dict = dict()
        #         # dictionary with keys of numbers and values of how often they showed up

        freq_dict = Counter(nums)
        c = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        print(freq_dict.items())
        res = []
        for i in range(k):
            res.append(c[i][0])
        return res

print(Solution().topKFrequent(nums = [1,1,1,1,1,1,2,2,2,2,3], k = 2))
