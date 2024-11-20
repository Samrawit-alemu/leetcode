class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
            n = len(grid)
            maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

            for i in range(1, n - 1):
                for j in range(1, n - 1):
                    # Initialize the maximum for the current 3x3 submatrix
                    max_value = 0
                    # Check the 3x3 submatrix centered at (i, j)
                    for x in range(i - 1, i + 2):
                        for y in range(j - 1, j + 2):
                            max_value = max(max_value, grid[x][y])
                    maxLocal[i - 1][j - 1] = max_value

            return maxLocal