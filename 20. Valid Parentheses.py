class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        para={')':'(','}':'{',']':'['}
    
        for ch in s:
            if ch in para:
                elem=stack.pop() if stack else '#'

                if para[ch]!= elem:
                    return False
            else:
                stack.append(ch)
        return not stack
                

    
