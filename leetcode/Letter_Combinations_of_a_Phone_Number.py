class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictn = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        
        if digits == "":
            return res
        
        
        
        if len(digits)==1:
            res = dictn[digits]
            return res
        elif len(digits)==2:    
            for i in dictn[digits[0]]:
                for j in dictn[digits[1]]:
                    temp = i+j
                    res.append(str(temp))
            return res
        
                    