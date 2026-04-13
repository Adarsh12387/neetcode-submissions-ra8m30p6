class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[]
        for i in range(len(nums)):
            t=1
            for j in range(len(nums)):
                if i!=j:
                    t=t*nums[j]
            prod.append(t)
        return prod