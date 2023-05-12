from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt_nums = Counter(nums)
        
        for num, cnt in cnt_nums.items():
            if cnt >= 2:
                return True
            
        return False
        