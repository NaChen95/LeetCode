

# -------------------  解法一：左闭右闭区间  -------------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        # 定义以下循环不变量（循坏刚开始时），：
        # [0, i) 已经遍历的数组
        # [0, j] 满足条件的数组，即 [0, j] 有序且无重复项
        j, i = 0, 0 # i = 0 或者 i = 1 都可以，但是从 1 开始更切合定义
        while i < len(nums):
            if nums[i] == nums[j]:
                i += 1
            else:
                j += 1 # 由于区间是 [0, j]，所以要填充的是下一个元素 j + 1
                nums[j] = nums[i]
                i += 1
        return j + 1 # [0, j] 的数组长度为 j + 1

# -------------------  解法二：左闭右开区间  -------------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        # 定义以下循环不变量（循坏刚开始时）：
        # 感觉定义成左闭右开的更自然，因为这样循环开始的时候，下标就是即将赋值的元素
        # [0, i) 已经遍历的数组
        # [0, j） 满足条件的数组，即 [0, j） 有序且无重复项
        j, i = 1, 1 # i = 0 或者 i = 1 都可以
        while i < len(nums):
            if nums[i] == nums[j - 1]:
                i += 1
            else:
                # 由于区间是 [0, j)，所以要填充的是下一个元素就是 j
                nums[j] = nums[i]
                i, j = i+1, j + 1
        return j # [0, j) 的数组长度为 j
