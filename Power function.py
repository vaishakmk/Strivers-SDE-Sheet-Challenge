'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        new_n = n
        if n<0:
            new_n = -1*n
        while new_n>0:
            if new_n%2==0:
                x = x*x
                new_n=new_n//2
            else:
                ans = ans*x
                new_n = new_n-1
        if n<0:
            ans = 1/ans
        return ans
            