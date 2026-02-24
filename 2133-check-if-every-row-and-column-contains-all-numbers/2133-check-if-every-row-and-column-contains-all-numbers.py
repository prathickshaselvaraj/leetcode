class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)

        for i in range(n):
            row_set = set()
            col_set = set()

            for j in range(n):
                if matrix[i][j] in row_set:
                    return False
                row_set.add(matrix[i][j])

                if matrix[j][i] in col_set:
                    return False
                col_set.add(matrix[j][i])

            if row_set != set(range(1, n+1)):
                return False
            if col_set != set(range(1, n+1)):
                return False

        return True