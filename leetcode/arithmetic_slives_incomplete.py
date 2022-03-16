class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        check = 0
        if len(nums) >= 3:
            for i in range(1,len(nums)):
                if i == 1:
                    check = nums[i]-nums[i-1]
                elif check != nums[i]-nums[i-1]:
                    return 0
                else:
                    pass
                
            counter = 0
            length = len(nums) - 3
            for i in range(1,length + 2):
                counter += i
            return counter
            
        else:
            return 0
        
        
# 3:1, 4:3, 5:6, 6:10, 7:15, 8:21, 9:28, 10:36, 11:45