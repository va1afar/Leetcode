class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        answer = ''
        list_sentence = sentence.split(' ')
        vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o','O', 'u', 'U']
        
        for i in range(len(list_sentence)):
            if list_sentence[i][0] in vowel:
                answer += list_sentence[i] + 'ma' + 'a' * (i+1) + ' '
            else:
                answer += list_sentence[i][1:] + list_sentence[i][0] + 'ma' + 'a' * (i+1) + ' '
            
        return answer[0:-1]