class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        con=[]
        count=0
        for i in nums:
            if i==0:
                con.append(count)
                count=0
                continue
            count+=1
        con.append(count)
        return max(con, default=0)