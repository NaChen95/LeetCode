
# -------------------  解法一：错误解法  -------------------
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        i, n = 0, len(intervals)
        res = []
        # 分三类讨论：左边不重叠，重叠，右边重叠
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        print("res1:", res)
        left, right = float("inf"), float("-inf") # 注意 Python3 里面正负无穷大的做法
        while i < n and newInterval[1] >= intervals[i][0]:
            left = min(left, intervals[i][0], newInterval[0])
            right = max(right, intervals[i][1], newInterval[1])
            i += 1
            print(left, right)
        if left < float("inf"): res.append([left, right])
        print("res2:", res)
        while i < n:
            res.append(intervals[i])
            i += 1
        print("res3:", res)
        return res
        
# -------------------  解法二：正确解法  -------------------
# https://leetcode.cn/problems/insert-interval/solutions/472435/shou-hua-tu-jie-57-cha-ru-qu-jian-fen-cheng-3ge-ji/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i, n = 0, len(intervals)
        res = []
        # 分三类讨论：左边不重叠，重叠，右边重叠
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # newInterval 一定要被插入，直接修改它
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res

# -------------------  还有一种解法是借鉴 LeetCode 56  -------------------
# 先插入，再套用 56 题的做法，也能过但是时间复杂度从 O(n) 变成了 O(nlgn)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for x in sorted_intervals:
            if (not res) or (x[0] > res[-1][1]):
                res.append(x)
            else:
                top = res.pop()
                res.append([top[0], max(top[1], x[1])])
        return res
