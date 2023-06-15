class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multiple_num = 1
        sum_num = 0
        
        for i in list(str(n)):
            multiple_num = multiple_num * int(i)
            sum_num += int(i)
            
        return multiple_num - sum_num
        
            