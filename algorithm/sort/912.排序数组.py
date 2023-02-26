
# -------------------  归并排序原地修改  -------------------
# 空间复杂度为 O(N)，因为 tmp 数组最大为 O(n)。栈帧空间为 O(lgn) https://leetcode.cn/circle/article/zeM9YK/
def merge_sort(nums, left, right): # 原地修改，[left, right]

    if left >= right:
        return
    
    mid = (left + right) >> 1 # [left, mid], [mid + 1, right]
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)

    tmp = [None] * (right - left + 1)
    i, j, k = left, mid + 1, 0

    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1
    if i > mid: tmp[k:] = nums[j:right + 1]
    if j > right: tmp[k:] = nums[i:mid + 1]
    nums[left:right + 1] = tmp[:]

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge_sort(nums, 0, len(nums) - 1)
        return nums

# -------------------  归并排序非原地修改  -------------------
# 空间复杂度应该也是 O(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1: return nums
        mid = (n - 1) >> 1
        # [0, mid], [mid + 1, n - 1]
        len1, len2 = mid + 1, n - 1 - (mid + 1) + 1
        nums1 = self.sortArray(nums[0:mid + 1]) 
        nums2 = self.sortArray(nums[mid + 1:n])
        tmp = [None] * n
        i = j = k = 0
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                tmp[k] = nums1[i]
                i += 1
            else:
                tmp[k] = nums2[j]
                j += 1
            k += 1
        if i >= len1: tmp[k:] = nums2[j:]
        if j >= len2: tmp[k:] = nums1[i:]
        return tmp

# ------------------- TODO 快速排序  -------------------