class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        answer = 0
        colMax = [0 for i in range(len(grid[0]))]
        rowMax = [0 for i in range(len(grid[0]))]
        
        # 各行、列の最大値をcolMax, rowMaxに保存します。
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                rowMax[row] = max(rowMax[row], grid[row][col])
                colMax[col] = max(colMax[col], grid[row][col])
        
        # 既存の行列をcolMax, rowMaxと比較し、追加可能な高さを計算します。
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                answer += min(rowMax[row], colMax[col]) - grid[row][col]
                
        return answer