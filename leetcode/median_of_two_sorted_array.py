class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = nums1 + nums2
        num3.sort()
        length = len(num3)
        if length%2==0:
            return (num3[length//2]+num3[(length//2) - 1])/2
        else:
            return num3[length//2]
        