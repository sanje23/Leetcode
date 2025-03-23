class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # Step 1: Check if first row and first column contain zeroes
        for j in range(col):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        for i in range(row):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Step 2: Use first row and first column as markers
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Set zeroes based on markers
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0

        for j in range(1, col):
            if matrix[0][j] == 0:
                for i in range(1, row):
                    matrix[i][j] = 0

        # Step 4: Set first row and first column if needed
        if first_row_zero:
            for j in range(col):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(row):
                matrix[i][0] = 0
