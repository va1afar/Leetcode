class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = ''
        for i in range(len(s)):
            answer += s[indices.index(i)]
            
        return answer