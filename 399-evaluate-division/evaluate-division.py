class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        # Build the graph
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        #  DFS function
        def dfs(curr, target, visited, product):
            if curr == target:
                return product

            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited, product * weight)
                    if res != -1:
                        return res

            return -1

        #  Process queries
        ans = []
        for x, y in queries:
            if x not in graph or y not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(x, y, set(), 1.0))

        return ans
