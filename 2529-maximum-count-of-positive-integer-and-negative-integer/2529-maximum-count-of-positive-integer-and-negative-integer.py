class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_cnt = 0
        pos_cnt = 0
        
        for num in nums:
            if num > 0:
                pos_cnt += 1
            elif num < 0:
                neg_cnt += 1
                
        return max(pos_cnt, neg_cnt)
            