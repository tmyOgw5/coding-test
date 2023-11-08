#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row * col -1

        while left <= right:
            mid = (left + right) // 2
            mid_element = matrix[mid // col][mid % col]
            if target == mid_element:
                return True
            elif target < mid_element:
                right = mid -1
            else:
                left = mid + 1
        return False

        


# @lc code=end

