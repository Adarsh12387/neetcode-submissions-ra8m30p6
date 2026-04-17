class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=set()
        for i in range(len(nums)-2):
            n1=nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                if n1+nums[j]+nums[k]==0:
                    ans.add((n1,nums[j],nums[k]))
                    j+=1
                    k-=1
                elif n1+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
        return list(ans)