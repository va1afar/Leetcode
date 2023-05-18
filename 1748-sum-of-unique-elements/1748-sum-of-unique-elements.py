from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        answer = 0
        cnt_nums = Counter(nums)
        
        for num, cnt in cnt_nums.items():
            if cnt == 1:
                answer += num
                
        return answer
        