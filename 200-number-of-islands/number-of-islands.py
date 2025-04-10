class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # [[False for i in range(len(grid[0]))] for _ in range(len(grid))]
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        cnt = 0

        def dfs(row, col):
            if row< 0 or row >= len(grid) or col<0 or col >= len(grid[0]) or grid[row][col]== "0":
                return 
            grid[row][col] = '0'#to show visited
            for i, j in direction:
                n_row, n_col = row + i, col + j
                dfs(n_row, n_col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i,j)
        return cnt
