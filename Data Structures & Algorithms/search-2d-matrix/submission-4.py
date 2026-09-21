from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        
        for row in range(rows):
            is_target_in_row = matrix[row][0] <= target and (
                row == rows - 1 or target < matrix[row + 1][0]
            )
            
            if is_target_in_row:
                left, right = 0, len(matrix[row]) - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    if target == matrix[row][mid]:
                        return True
                    elif target < matrix[row][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1                        
                return False
                
        return False