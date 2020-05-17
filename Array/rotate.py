def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        1.通过两步操作达到旋转的效果：a转置（转置一次后要分到小块），b垂直镜像
        """
        # n = len(matrix)
        # for i in range(n//2):
        #     matrix[i][:], matrix[n-i-1][:] = matrix[n-i-1][:], matrix[i][:]
        
        # matrix[:] = [[matrix[i][j] for i in range(n)] for j in range(n)] 
        # print(1)


        '''
        '''
        # n = len(matrix[0])        
        # # transpose matrix
        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        
        # # reverse each row
        # for i in range(n):
        #     matrix[i].reverse()


        '''
        1.想象成四个小方块依次旋转
        '''
        n = len(matrix[0])        
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
        


# rotate([[1,2,3],[4,5,6],[7,8,9]])
rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])
