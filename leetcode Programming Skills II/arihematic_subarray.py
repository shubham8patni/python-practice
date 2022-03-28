class Solution:
    def checkArithmeticSubarrays(self, nums, l, r) :
        ans = []
        fins = []
        if len(nums)==2:
            return "True"
        for i in range(len(l)):
            temp = nums[l[i] : r[i]+1]
            temp.sort()
            diff = temp[1] - temp[0]
            is_arithmetic = True
            for i in range(1,len(temp) - 1):
                if temp[i + 1] - temp[i] != diff:
                    is_arithmetic = False
                    break
            fins.append(is_arithmetic)
        return fins