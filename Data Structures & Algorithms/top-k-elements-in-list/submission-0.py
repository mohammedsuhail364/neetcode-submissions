class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        li=[]
        c1=dict(sorted(c.items(),key=lambda x:x[1],reverse=True))
        topFrequencyElement=0
        for key in c1.keys():
            if topFrequencyElement<k:
                li.append(key)
                topFrequencyElement+=1
        return li