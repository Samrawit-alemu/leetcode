class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        visited = set()
        n = len(isConnected)

        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    dfs(j)
            return 
        for i in range(n):
            if i not in visited:
                province += 1
                dfs(i)
        return province