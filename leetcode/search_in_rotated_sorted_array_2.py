class Solution:
    def search(self, nums, target):
        if target in nums:
            return True
        else:
            False




class Solution:
    def search(self, nums, target):
        nums.sort()
        for i in nums:
            if i>target:
                return False
            if i==target:
                return True
        return False