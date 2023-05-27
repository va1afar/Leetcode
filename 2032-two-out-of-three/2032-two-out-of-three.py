class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        l = []
        
        for i in nums1:
            if i in nums2 or i in nums3:
                l.append(i)
        for j in nums2:
            if j in nums1 or j in nums3:
                l.append(j)
                
        return set(l)
        
        