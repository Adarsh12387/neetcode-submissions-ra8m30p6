class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=len(s)
        if j==0:
            return True
        for char in t:
            #print(char,s[i])
            if i!=j:
                if char==s[i]:
                    #print(i)
                    i+=1
        #print(i,j)
        if i==j:
            return True
        else:
            return False