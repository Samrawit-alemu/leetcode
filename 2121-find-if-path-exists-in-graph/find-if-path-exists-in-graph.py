class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        stk = [source]
        visited = set([source])

        while stk:
            node = stk.pop()
            if node == destination:
                return True

            for neighbour in graph[node]:
                if neighbour not in visited:
                    stk.append(neighbour)
                    visited.add(neighbour)
        return False
        