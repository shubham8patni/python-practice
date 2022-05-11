class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
		
		# s = start of iteration - to avoid repetitions
		# tmp - temp list holding possible combination
		# l - keep track of length of tmp
        def rec(k, n, s, tmp, l):
            if l == k:
                # return True to break out of loop
				# we can't get another answer from combination from here
				# only combinations with sum greater than n
                if sum(tmp) == n:
                    ans.append(tmp)
                    return True
                return False
           
            for i in range(s, 10):
                if rec(k, n, i+1, tmp+[i], l+1):
                    break
					
        rec(k, n, 1, [], 0)
        return ans