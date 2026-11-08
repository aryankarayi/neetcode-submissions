class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Row
        for row in range(9):
            seen = []
            for column in range(9):
                if board[row][column] in seen:
                    return False
                elif board[row][column] != '.':
                    seen.append(board[row][column])
        # Check Column
        for col in range(9):
            seen = []
            for row in range(9):
                if board[row][col] in seen:
                    return False
                elif board[row][col] != '.':
                    seen.append(board[row][col])
        
        for down_shift in range(0, 9, 3):
            for right_shift in range(0,9,3):
                seen = []
                for row in range(3):
                    for col in range(3):
                        if board[row + down_shift][col + right_shift] in seen:
                            return False
                        elif board[row + down_shift][col + right_shift] != '.':
                            seen.append(board[row + down_shift][col + right_shift])

        return True