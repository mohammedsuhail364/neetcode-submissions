class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=sorted(list(set(nums)))
        count=0
        li=[]
        if len(set1)==0:
            return 0
        if len(set1)==1:
            return 1
        for i in range(len(set1)-1):
            if set1[i]+1==set1[i+1]:
                count+=1
                if i==len(set1)-2:
                    li.append(count)
            else:
                li.append(count)
                count=0
        return max(li)+1