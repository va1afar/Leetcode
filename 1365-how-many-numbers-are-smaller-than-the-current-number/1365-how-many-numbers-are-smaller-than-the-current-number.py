class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        
        for num_1 in nums:
            smaller_count = 0
            for num_2 in nums:
                if num_1 > num_2:
                    smaller_count += 1
            answer.append(smaller_count)
            
        return answer
            
        
        
        