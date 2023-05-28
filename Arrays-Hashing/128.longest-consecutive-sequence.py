#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                longest = max(longest, length)
        return longest
        
# @lc code=end

