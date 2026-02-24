class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value=board[r][c]
                if value==".":
                    continue
                index=(r//3)*3 +(c//3)
                if value in rows[r]:
                    return False
                if value in cols[c]:
                    return False
                if value in boxes[index]:
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                boxes[index].add(value)
        return True
