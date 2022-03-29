class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                return nums[i] 