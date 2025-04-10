class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    
        graph = defaultdict(list)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        # print(graph)
        color = [-1] * (n+1)

        for i in range(1,n+1):
            if color[i] == -1:
                color[i] = 0
                stk = [i]

                while stk:
                    curr = stk.pop()
                    for neighbour in graph[curr]:
                        if color[neighbour] == -1:
                            color[neighbour] = 1 - color[curr]
                            stk.append(neighbour)
                          

                        else:
                            if color[neighbour] == color[curr]:
                                return False
        return True