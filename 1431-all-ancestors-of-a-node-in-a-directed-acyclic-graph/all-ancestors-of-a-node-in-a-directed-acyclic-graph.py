class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for a,b in edges:
            graph[b].append(a)

        memo = {}

        def dfs(node: int) -> Set[int]:
            if node in memo:
                return memo[node]

            ancestors = set()
            for parent in graph[node]:
                ancestors.add(parent)
                ancestors.update(dfs(parent))
            
            memo[node] = ancestors
            return ancestors

        ans = []
        for i in range(n):
            result = sorted(dfs(i)) 
            ans.append(result)

        return ans