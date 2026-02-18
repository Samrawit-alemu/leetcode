class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in r for r in matrix)