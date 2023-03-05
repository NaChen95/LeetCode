class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        #nums.sort()
        i = j = 0
        while i < n:
            if nums[i] != val:
                nums[j] = nums[i]
                i, j = i+1, j+1
            else:
                i += 1
        return j

