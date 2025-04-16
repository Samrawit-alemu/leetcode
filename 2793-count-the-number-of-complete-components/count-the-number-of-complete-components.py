class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        
        complete = 0

        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour, component)

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)

                num_node = len(component)
                num_edges = sum(len(graph[node]) for node in component) // 2
                if num_edges == num_node * (num_node - 1) // 2:
                    complete += 1
        return complete 