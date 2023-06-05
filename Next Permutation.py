'''
For example, for arr = [1,2,3], the following are all the permutations of arr: 
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        break_point = -1

        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                break_point = i
                break
        
        if break_point==-1:
            nums[:] = nums[::-1]
            return
        for i in range(n-1,break_point,-1):
            if nums[i]>nums[break_point]:
                nums[i],nums[break_point]= nums[break_point],nums[i]
                break
        nums[:] = nums[0:break_point+1]+list(reversed(nums[break_point+1:]))
        return 
