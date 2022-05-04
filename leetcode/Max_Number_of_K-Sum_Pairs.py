class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)//2):
            print(nums[i])