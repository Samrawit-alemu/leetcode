class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] *n
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                stk = [node]

                while stk:
                    curr = stk.pop()

                    for i in graph[curr]:
                        if color[i] == -1:
                            color[i] = 1- color[curr]
                            stk.append(i)
                        else:
                            if color[i] == color[curr]:
                                return False

        return True
































        # def dfs(node, graph):
        #     temp = True
        #     for neighbour in graph[node]:
        #         if color[neighbour] == -1:
        #             if color[node] == 0:
        #                 color[neighbour] = 1
        #             else:
        #                 color[neighbour] = 0
        #                 temp = temp and dfs(neighbour, graph)
        #         elif color[neighbour] == color[neighbour]:
        #             return False
        #     return temp  

        #     r = [-1 for _ in range(len(graph))]
        #     result = True
        #     for node in range(n):
        #         if color[node] == -1:
        #             color[node] = 0
        #             result = result and dfs(node, graph)
        #     return result
            # #0 blue, 1 red, -1 colorless 

        # colors = [-1 for _ in range(len(graph))]

        # def dfs(node,color):
        #     if color[node] != -1:
        #         return 

        #     color[node] = 
            # for