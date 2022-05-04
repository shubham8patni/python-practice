class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)//2):
            if nums[i] + nums[(len(nums)-1)-i] == k:
                count += 1
            else:
                pass
        return count