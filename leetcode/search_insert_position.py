class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return (len(nums))
        elif target not in nums:
            for i in range(len(nums)):
                if nums[i] >target:
                    return i
        elif target in nums:
            return nums.index(target)