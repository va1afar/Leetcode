from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt_moves = Counter(list(moves))
        
        if cnt_moves['U'] == cnt_moves['D'] and cnt_moves['L'] == cnt_moves['R']:
            return True
        else:
            return False
        
        