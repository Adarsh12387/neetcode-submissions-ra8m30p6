class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(t):
            temp={}
            for i in t:
                if i not in temp:
                    temp[i]=1
                else:
                    temp[i]+=1
            return temp
        return count(s)==count(t)