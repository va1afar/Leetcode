class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_A, sum_B = sum(aliceSizes), sum(bobSizes)
        set_B = set(bobSizes)
        
        for x in aliceSizes:
            if x + (sum_B - sum_A) / 2 in set_B:
                return [x, x + (sum_B - sum_A) / 2]