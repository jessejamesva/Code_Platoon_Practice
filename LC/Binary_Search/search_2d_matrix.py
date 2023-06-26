def searchMatrix(matrix, target):
        for i in matrix:
            if target <= i[-1]:
                print(i)
                if target in i:
                    return True
                

        else: return False