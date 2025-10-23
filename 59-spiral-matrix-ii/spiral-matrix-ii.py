class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]

        l,r = 0, n-1
        t,b = 0, n-1
        val = 1

        while l <= r:
            for c in range(l, r+1):
                mat[t][c] = val
                val += 1
            t += 1
            for k in range(t, b+1):
                mat[k][r] = val
                val += 1
            r -= 1
            for c in range(r, l-1, -1):
                mat[b][c] = val
                val += 1
            b -= 1
            for k in range(b, t-1, -1):
                mat[k][l] = val
                val += 1
            l += 1
        return mat
