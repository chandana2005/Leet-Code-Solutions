'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''
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
                

    
