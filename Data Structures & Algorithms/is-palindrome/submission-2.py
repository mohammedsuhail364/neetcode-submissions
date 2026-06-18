class Solution:
    def isPalindrome(self, s: str) -> bool:
        li=[]
        for i in s:
            if 'A'<=i<='Z' or 'a'<=i<='z':
                li.append(i.lower())
            elif  i in '1234567890':
                li.append(i)
        
        if li==li[::-1]:
            return True
        return False
       
