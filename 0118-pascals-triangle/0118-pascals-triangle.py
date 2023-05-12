class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        
        for i in range(1, numRows+1): 
            if i == 1:
                answer.append([1])
            elif i == 2:
                answer.append([1,1])
            else:
                tmp_list = []
                for j in range(0, i):
                    if j == 0 or j == i-1:
                        tmp_list.append(1)
                    else:
                        tmp_list.append(answer[-1][j-1] + answer[-1][j])
                answer.append(tmp_list)
        
        return answer
        