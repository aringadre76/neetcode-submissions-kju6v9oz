class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find ROW
        l, r = 0, len(matrix)-1

        r_idx = None

        while l <= r:
            m = (l + r) // 2

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][len(matrix[0])-1]:
                l = m + 1

            else: 
                r_idx = m
                break
        
        if r_idx is None: return False

        print(r_idx)

        # find target in ROW
        ROW = matrix[r_idx]

        l, r = 0, len(ROW)-1



        while l <= r:
            m = (l + r) // 2

            if target < ROW[m]:
                r = m - 1

            elif target > ROW[m]:
                l = m + 1
            
            else:
                return True
        
        return False



        




