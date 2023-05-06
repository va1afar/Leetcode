from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_nums = Counter(nums)
        for key, value in cnt_nums.items():
            if value == 1:
                return key