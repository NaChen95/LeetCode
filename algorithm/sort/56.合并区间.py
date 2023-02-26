"""
这一题的关键是想到对左端点进行排序，然后按照直观思维，将区间一个个送入判断即可
另外注意 Python3 自定义排序的做法

"""

from functools import cmp_to_key

def my_cmp(x1, x2):
    # 前者减去后者，是升序
    # 如果是字符串不能相减，而要用比较运算符
    return x1[0] - x2[0]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=cmp_to_key(my_cmp))
        # 或者改成： sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for x in sorted_intervals:
            if (not res) or (x[0] > res[-1][1]):
                res.append(x)
            else:
                top = res.pop()
                res.append([top[0], max(top[1], x[1])])
        return res