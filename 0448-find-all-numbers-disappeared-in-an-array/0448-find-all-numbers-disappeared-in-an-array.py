from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        dict_nums = {}
        cnt_nums = Counter(nums)
        
        # Creating a Dictionary
        for i in range(1, len(nums)+1):
            dict_nums[i] = False
            
        for j in cnt_nums:
            del dict_nums[j] 
            
        for k in dict_nums:
            answer.append(k)
                
        return answer
        
        

            
        