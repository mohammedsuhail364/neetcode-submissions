class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                s1=s[i:j]
                if s!="" and len(s1)==len(set(s1)):
                    if len(s1)>max1:
                        max1=len(s1)
        return max1