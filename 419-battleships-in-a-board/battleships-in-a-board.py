class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    if r > 0 and board[r - 1][c] == 'X':
                            continue 
                    if c > 0 and board[r][c - 1] == 'X':
                            continue 
                    cnt += 1
        return cnt
