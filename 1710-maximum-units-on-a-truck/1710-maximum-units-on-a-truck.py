class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sum_of_units = 0
        
        boxTypes.sort(key=lambda x:(x[1], x[0]), reverse=True)
        for box in boxTypes:
            if truckSize - box[0] > 0:
                sum_of_units += box[1] * box[0]
                truckSize -= box[0]
            elif truckSize - box[0] == 0:
                sum_of_units += box[1] * box[0]
                break
            else:
                sum_of_units += box[1] * truckSize
                break
        
        return sum_of_units
            
                    
                
            