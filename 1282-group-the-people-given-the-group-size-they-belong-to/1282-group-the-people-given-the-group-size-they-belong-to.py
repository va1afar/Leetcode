class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        graph = collections.defaultdict(collections.deque)
        
        for idx, i in enumerate(groupSizes):
            graph[i].append(idx)
            
        result = []
        
        for key, val in graph.items():
            while val:
                tmp = []
                for i in range(key):
                    tmp += [val.popleft()]
                result.append(tmp)                
        
        return result     