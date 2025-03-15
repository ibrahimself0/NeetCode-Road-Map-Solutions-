from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        col = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r // 3, c // 3)]:
                    return False
                else:
                    col[c].add(board[r][c])
                    row[r].add(board[r][c])
                    square[(r // 3, c // 3)].add(board[r][c])
        return True
