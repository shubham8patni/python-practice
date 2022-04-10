class Solution:
    def topKFrequent(self, nums, k):
        cnt = Counter(nums)
        if len(nums)==1:
            return nums
        sol = []
        for i in cnt.most_common(k):
            sol.append(i[0])
        return sol