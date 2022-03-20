class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        arr = []
        if len(haystack) == 0 and len(needle)==0:
            return 0
        elif len(haystack) == 0 and len(needle)!=0:
            return -1
        elif len(haystack) != 0 and len(needle)==0:
            return 0
        arr = haystack.split(needle)
        if arr[0] == haystack:
            return -1
        else:
            return len(arr[0])