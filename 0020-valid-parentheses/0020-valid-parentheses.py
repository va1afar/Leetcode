class Solution:
    def isValid(self, s: str) -> bool:
        # using 'stack' structure
        stack_s = []
        
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack_s.append(ch)
            elif ch == ')' and stack_s and stack_s.pop() == '(':
                continue
            elif ch == ']' and stack_s and stack_s.pop() == '[':
                continue
            elif ch == '}' and stack_s and stack_s.pop() == '{':
                continue
            else:
                return False
        if stack_s:
            return False
        
        return True
        
         
                
    
        
        
        
        