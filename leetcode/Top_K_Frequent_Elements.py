class Solution:
    def topKFrequent(self, nums, k):
        if len(nums)==1:
            return nums
        sol = []
        for i in Counter(nums).most_common(k):
            sol.append(i[0])
        return sol