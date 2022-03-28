class Solution:
    def kClosest(self, points, k: int):      
        lt = []
        ans=[]
        if len(points)==k:
            return points
        for i in points:
            temp = (i[0]*i[0])+(i[1]*i[1])
            lt.append([temp,i])
        lt.sort()
        for i in range(k):
            ans.append(lt[i][1])
        return ans
