'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

'''


class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        slow = arr[0]
        fast = arr[0]
        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow==fast:
                break
            
        fast = arr[0]
        if slow == fast:
                return slow
        while True:
            slow = arr[slow]
            fast = arr[fast]
            if slow == fast:
                return slow