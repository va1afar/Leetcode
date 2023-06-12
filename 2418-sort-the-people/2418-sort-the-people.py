class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        answer = []
        idx_list = []
        
        zip_list = list(zip(heights, names))
        zip_list.sort(reverse=True)
        
        for i in zip_list:
            answer.append(i[1])
        
        return answer
            