#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openN,closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN+1,closeN)
                stack.pop()
                
            if closeN < openN:
                stack.append(')')
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return res
            
        
        
# @lc code=end

