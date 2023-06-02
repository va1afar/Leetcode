class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = [int(ball) for ball in boxes]
        boxes_having_balls =  [i for i in range(len(balls)) if balls[i] == 1]
        results = []
        
        for i in range(len(balls)):
            result = 0
            for box in boxes_having_balls:
                result = result + abs(i - box)
            results.append(result) 
            
        return results     