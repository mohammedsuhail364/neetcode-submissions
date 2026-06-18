class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            k=nums[i]
            nums[i]=1
            res.append(math.prod(nums))
            nums[i]=k
        return res
