class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        while len(str_num) > 1:
            tmp = 0
            for ch in list(str_num):
                tmp += int(ch)
            str_num = str(tmp)
        
        return int(str_num)
        