class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        max_candy = max(candies) - extraCandies
        
        for candy in candies:
            if candy >= max_candy:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer
        
        