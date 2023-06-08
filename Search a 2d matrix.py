'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        m = len(matrix)
        n = len(matrix[0])
        end = m*n-1
        while start<=end:
            mid = start + (end-start)//2
            row = mid//n 
            col = mid - row*n
            # print(mid)
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                start = mid+1
            else:
                end = mid-1
        return False