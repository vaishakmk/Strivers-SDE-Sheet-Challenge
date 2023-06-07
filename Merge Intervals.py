'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_intervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            new_start = interval[0]
            new_end = interval[1]
            if new_start<=end:
                end = max(end,new_end)
            else:
                new_intervals.append([start,end])
                start = new_start
                end = new_end
        
        new_intervals.append([start,end])
        return new_intervals
        