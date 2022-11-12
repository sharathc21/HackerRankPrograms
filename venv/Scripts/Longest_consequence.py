class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        numsSet = set(nums)

        longestSeq = 0

        for each in nums:
            print("Printing Each", each)

            if each - 1 not in numsSet:
                print("entered if loop", each-1)

                length = 0

                while (each + length in numsSet):
                    print("in while loop", each + length)
                    length += 1

                longestSeq = max(length, longestSeq)
                print("Longest as of now", longestSeq)

        return longestSeq

print(Solution().longestConsecutive([5,2,7,8, 9,6, 3,2,1,0, 12, 14, 13, 18, 17, 15, 16, 19, 21, 20, 11]))