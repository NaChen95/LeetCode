# 循环不变量（循环过程中总是成立的断言/性质）：https://www.bilibili.com/video/BV1Jg411M7Lp/?spm_id_from=333.337.search-card.all.click&vd_source=683a01bdc1972c35f5b27445f6fa8ccd
# 有点类似于数学归纳，最好将它作为注释写在代码中
# -------------------  解法一：遍历了数字两次  -------------------
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1
        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count0 + count1):
            nums[i] = 1
        for i in range(count0 + count1, count0 + count1 + count2):
            nums[i] = 2

# -------------------  解法二：只遍历一次，常数空间  -------------------
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        n = len(nums)

        # [0, p0) => 全零
        # [p0, p1) => 全1
        # (p2, n) => 全2，注意 p1 和 p2 一开始是断续的，并且 p2 是开区间（每轮循坏开始时都是即将填充的位置）
        p0, p1, p2 = 0, 0, n - 1 # 初始值均为空集
        # 为什么要以 p1 作为循环变量呢？
        while p1 <= p2:
            if nums[p1] == 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
                #p1, p2 = p1+1, p2-1 #不能这样写，因为交换回来的元素不一定是 1，需要下一轮来判断！
            elif nums[p1] == 1:
                p1 += 1
            else:
                nums[p1], nums[p0] = nums[p0], nums[p1] # 也可以直接用 nums[p1], nums[p0] = 1, 0
                p1, p0 = p1+1, p0+1

# -------------------  解法三：修改循环不变量 p2 的定义  -------------------
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        n = len(nums)

        # [0, p0) => 全零
        # [p0, p1) => 全1
        # [p2, n) => 全2，注意 p1 和 p2 一开始是断续的

        p0, p1, p2 = 0, 0, n
        # 为什么要以 p1 作为循环变量呢？
        while p1 < p2:
            if nums[p1] == 2:
                p2 -= 1
                nums[p1], nums[p2] = nums[p2], nums[p1]                
            elif nums[p1] == 1:
                p1 += 1
            else:
                nums[p1], nums[p0] = nums[p0], nums[p1]
                p1, p0 = p1+1, p0+1

# -------------------  解法四：将 p2 从右往左遍历  -------------------
# 为什么要以 p1 来遍历循环呢？首先 p0 肯定不行，因为它的右边一位是 1，不能主动向右走。
# 可以用 p2 从右往左遍历：
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        n = len(nums)
        # [0, p0) => 全零
        # [p0, p1) => 全1
        # (p2, n) => 全2，注意 p1 和 p2 一开始是断续的，并且 p2 是开区间（每轮循坏开始时都是即将填充的位置）
        p0, p1, p2 = 0, 0, n - 1 # 初始值均为空集
        while p1 <= p2:
            if nums[p2] == 2:
                p2 -= 1
            elif nums[p2] == 1:
                nums[p2], nums[p1] = nums[p1], nums[p2]
                p1 += 1
            else: # nums[p2] == 0
                nums[p2] = nums[p1]
                nums[p0] = 0
                if p1 > p0: nums[p1] = 1
                p0, p1 = p0+1, p1+1
                # 不能加上 p2 -= 1，因为换过来的不一定是 2