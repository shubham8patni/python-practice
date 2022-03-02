class Solution:
    def countBits(self, n: int) -> List[int]:
        #print(f"{n:b}")
        counter = 0
        temp = 0
        ans = []
        for i in range(n+1):
            temp = f"{i:b}"
            for i in temp:
                if i =="1":
                    counter +=1
                else:
                    pass    
            ans.append(counter)
            counter = 0
            
        return ans