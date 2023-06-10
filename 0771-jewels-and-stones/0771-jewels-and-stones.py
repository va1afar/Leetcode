class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        
        for ch_stones in stones:
            for ch_jewels in jewels:
                if ch_jewels == ch_stones:
                    answer += 1
        
        return answer
                    