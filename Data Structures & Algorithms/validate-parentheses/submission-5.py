class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = []
        for i in s:
            if i in ['(','{','[']:
                paranthesis.append(i)
            elif i in [')','}',']']:
                if not paranthesis:
                    return False
                elif (paranthesis[-1]=='(' and i==')') or (paranthesis[-1]=='{' and i=='}') or (paranthesis[-1]=='[' and i==']'):
                    paranthesis.pop()
                else:
                    return False
        if len(paranthesis)==0:
            return True
        else:
            return False