class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) - 1
            while l <= r:
                mid = ((r - l) // 2) + l

                if matrix[i][l] == target or matrix[i][r] == target:
                    return True

                if matrix[i][mid] == target:
                    return True

                if matrix[i][mid] > target:
                    r = mid - 1

                if matrix[i][mid] < target:
                    l = mid + 1
        return False
                

        