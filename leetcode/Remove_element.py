class Solution:
    def removeElement(self, nums, val: int) -> int:
        count = 0
        while val in nums:
            nums.remove(val)
            count += 1
        print(count, nums)