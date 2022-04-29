class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col = [-1]*n
        for i in range(n):
            if col[i]!=-1:
                continue
            q = deque()
            q.append((i,0))
            print(q)