class Solution:
    def lengthOfLastWord(self, s: str):
        ls = s.split()
        return len(ls[-1])