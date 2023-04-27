class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        answer = ''
        list_s = s.split(' ')
        list_s.sort()
        
        for s in list_s:
            answer += str(s)[-1:0:-1] + ' '
        answer = answer[:-1]
        
        
        return answer
             
            
            
            
        
        