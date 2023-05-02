class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        
        if len(nums) <= 1:
            return 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                answer += nums[i-1] - nums[i] + 1
                nums[i] += nums[i-1] - nums[i] + 1
                
        return answer
            