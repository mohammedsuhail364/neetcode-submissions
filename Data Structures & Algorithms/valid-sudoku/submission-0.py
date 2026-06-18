class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_rows=defaultdict(set)
        set_cols=defaultdict(set)
        sub_boxes=defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]=='.':
                    continue
                value=board[r][c]
                if value in set_rows[r] or value in set_cols[c] or value in sub_boxes[r//3,c//3]:
                    return False
                set_rows[r].add(value)
                set_cols[c].add(value)
                sub_boxes[r//3,c//3].add(value)
        return True
