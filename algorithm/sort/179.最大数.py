from functools import cmp_to_key

def mycmp(nums1, nums2):
    return -1 if nums1 + nums2 > nums2 + nums1 else 1

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        sorted_nums = sorted(nums, key=cmp_to_key(mycmp))
        print(sorted_nums)
        res = ""
        for num in sorted_nums:
            res += num
        return str(int(res)) # 去除前面的零，由于是找的最大数，所以也可以只通过判断第一位数是不是零来