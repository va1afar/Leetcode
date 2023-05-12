class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = 0
        s_list = s.split(' ')
        
        for s in s_list:
            if s.isalpha():
                answer = len(s)
                
        return answer