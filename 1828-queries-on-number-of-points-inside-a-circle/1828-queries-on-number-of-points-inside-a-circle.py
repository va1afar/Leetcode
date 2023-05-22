class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        
        # 直角三角形の性質である、a^2 + b^2 = c^2 (cは対角線)を逆に利用し、
        # a^2 + b^2 が query[2]**2以下かどうか確認します。
        for query in queries:
            dots_in_query = 0
            for point in points:
                if sqrt((query[0] - point[0])**2 + (query[1] - point[1])**2) <= query[2]:
                    dots_in_query += 1
            answer.append(dots_in_query)
            
        return answer
                    