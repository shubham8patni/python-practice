class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        N = len(equations)
        for i in range(N):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1/values[i]
            

        def dfs(x,y,visited):
            print(x,y,visited)


        output = []
        for p,q in queries:
            output.append(dfs(p, q, set()))
        