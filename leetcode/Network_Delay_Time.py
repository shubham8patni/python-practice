class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        
        for x,y,w in times:
            adj_list[x].append((w, y))

        print(adj_list)