import enum

class solution:

    class direction(enum.Enum):
        RIGHT = 0,
        DOWN = 1,
        LEFT = 2,
        UP = 3


    def printSpiral(self, arr: list, m: int, n: int):
        """ The method prints a 2D array in a spiral form.
        
        Parameters
        ----------
            arr: list
                the 2 D array to print\n
            m: int
                the number of rows\n
            n: int
                the number of columns
        """
        (top, bottom) = (0, m-1) # variables for managing rows
        (left, right) = (0, n-1) # variables for managing columns

        # direction can be denoted by 0, 1, 2, 3
        # 0 = Right; 1 = Down; 2 = left; 3 = up
        # dir = self.direction.RIGHT
        dir = 0

        while top <= bottom and left <= right:
            # if dir == self.direction.RIGHT:
            if dir == 0:
                i = left
                while i <= right:
                    print(arr[top][i], end = " ")
                    i += 1
                top += 1
                # dir = self.direction.DOWN
            # elif dir == self.direction.DOWN:
            elif dir == 1:
                i = top
                while i <= bottom:
                    print(arr[i][right], end = " ")
                    i+= 1
                right -= 1
                # dir = self.direction.LEFT
            # elif dir == self.direction.LEFT:
            elif dir == 2:
                i = right
                while i >= left:
                    print(arr[bottom][i], end = " ")
                    i -= 1
                bottom -= 1
                # dir = self.direction.UP
            # elif dir == self.direction.UP:
            elif dir == 3:
                i = bottom
                while i >= top:
                    print(arr[i][left], end = " ")
                    i -= 1
                left += 1
                # dir = self.direction.RIGHT
            dir = (dir+1)%4
        print("")
        


    def printSpiral2D(self, arr, i, j, m, n):
        """ The method prints a 2D array in a spiral form.
        
        Parameters
        ----------
            arr: list
                the 2 D array to print\n
            i: int
                starting index for rows\n
            j: int
                starting index for cols\n
            m: int
                ending index for rows\n
            n: int
                ending index for cols\n
        """
        if i >= m and j >= n: return

        for p in range(i, n):
            print(arr[i][p], end= " ")
        
        for p in range(i+1, m):
            print(arr[p][n-1], end = " ")
        
        if m-1 != i:
            for p in range(n-2, j-1, -1):
                print(arr[m-1][p], end=" ")
        
        if n-1 != j:
            for p in range(m-2, i, -1):
                print(arr[p][j], end=" ")
        
        self.printSpiral2D(arr, i+1, j+1, m-1, n-1)


sol = solution()
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
sol.printSpiral(arr, 4, 4)
sol.printSpiral2D(arr, 0, 0, 4, 4)
print("\n")