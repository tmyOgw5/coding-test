#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # create hashMaps for both strings
        countS, countT = {}, {}
        for i in range(len(s)):
            # if not in dict, return 0, prevent key error
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
            
        for c in countS:
            # check if the key is in the other dict
            if countS[c]!=countT.get(c, 0):
                return False
        return True
        
        
# @lc code=end

