class Solution:
    def isMonotonic(self, nums):
        asc = sorted(nums)
        des = asc[::-1]
        if asc==nums:
            return True
        if des == nums:
            return True
        return False
    