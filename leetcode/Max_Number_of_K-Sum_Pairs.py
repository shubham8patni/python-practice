class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        count = 0
        for i in nums:
            remain = k - i
            if counter[remain]>0:
                counter[remain]-=1
                count+=1
            else:
                counter[i] +=1
            #print(remain, count,counter)

        return count