#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([c for c in s if c.isalnum()])
        return s == s[::-1]
# @lc code=end

