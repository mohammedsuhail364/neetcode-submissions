class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        res=0
        for i in s:
            if i !=")":
                stack.append(i)
                res=max(res,stack.count("("))
            elif i==")":
                while stack and stack[-1]!="(":
                    stack.pop()
                stack.pop()
        return res