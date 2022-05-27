class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==0:
            return 0
        ans=0
        while num>1:
            if num%2==1:
                ans+=1
            num=num//2
            ans+=1
        return ans+1