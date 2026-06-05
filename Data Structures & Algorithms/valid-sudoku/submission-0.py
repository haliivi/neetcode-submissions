class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if (cur == '.'):
                    continue
                if (
                    cur in rows[r] or
                    cur in cols[c] or
                    cur in squares[(r // 3, c // 3)]
                ):
                    return False
                rows[r].add(cur)
                cols[c].add(cur)
                squares[(r // 3, c // 3)].add(cur)
        return True

