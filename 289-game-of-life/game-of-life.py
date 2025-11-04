class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                live_neighb = 0

                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if (i == r and j == c) or not(0 <= i < rows and 0 <= j < cols):
                            continue
                        if board[i][j] == 1 or board[i][j] == -1:
                            live_neighb += 1
                
                if board[r][c] == 1 and (live_neighb <2 or live_neighb > 3):
                    board[r][c] = -1
                if board[r][c] == 0 and live_neighb == 3 :
                    board[r][c] = 2
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
                

        