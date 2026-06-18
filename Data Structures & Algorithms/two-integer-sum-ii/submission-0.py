class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li={}
        for i,value in enumerate(numbers):
            complement=target-value
            if complement in li:
                return [li[complement]+1,i+1]
            li[value]=i
        
