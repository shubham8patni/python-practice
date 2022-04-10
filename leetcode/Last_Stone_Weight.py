class Solution:
    def lastStoneWeight(self, stones):
        stones.sort(reverse=True)
        i=0
        if len(stones)==1:
            return stones[0]
        if len(stones)==2:
            if stones[0] == stones[1]:
                return 0
        
        while len(stones)!=1:   
            if len(stones)==0:
                break
            stones[i+1]=abs(stones[i]-stones[i+1])
            if stones[i+1] == 0:
                stones = stones[2:]           
            else:                
                stones = stones[1:]
            stones.sort(reverse=True)          
        if len(stones)==0:
            return 0
        else:
            return stones[0]