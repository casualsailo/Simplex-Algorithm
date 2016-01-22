def main():
    matrix = [[1,2,1,0,40], [4,3,0,1,120], [-40,-50,0,0,0]]
    #print(matrix)
    #print()
    #simplex_algorithm(matrix)

    print()
    matrix = [[1,2,5,1,0,0,40],[4,3,7,0,1,0,120],[5,7,6,0,0,1,150],[-40,-50,-80,0,0,0,0]]
    print(matrix)
    print()
    simplex_algorithm(matrix)

    print()
    matrix = [[1,2,5,10,1,0,0,0,40],[4,3,7,1,0,1,0,0,120],[5,7,6,2,0,0,1,0,150],[6,1,8,7,0,0,0,1,130],[-40,-50,-80,-200,0,0,0,0,0]]
    #print(matrix)
    #print()
    #simplex_algorithm(matrix)


def simplex_algorithm(matrix):
    #create a set that checks if the row has been done
    done = set()
    
    #obtain the amount of rows & columns
    rows = len(matrix)
    columns = len(matrix[0])
    num = int((columns - 1) - (columns - 1)/2)

    #use simplex algorithm n times for the number of variables
    for n in range (0, num):
        #obtain the minimum pivot row
        Xmin = matrix[0][len(matrix[0])-1]/matrix[0][n]
        Xrow = 0
        for i in range (0, rows-1):
            if i not in done:
                if Xrow in done:
                    Xmin = matrix[i][len(matrix[i])-1]/matrix[i][n]
                    Xrow = i
                temp = matrix[i][len(matrix[i])-1]/matrix[i][n]
                if (Xmin > temp):
                    Xmin = temp
                    Xrow = i
  
        done.add(Xrow)
        
        #normalize the pivot row
        temp = matrix[Xrow][n]
        for i in range (0, columns):
            matrix[Xrow][i] = matrix[Xrow][i]/temp

        #row reduction operation
        for i in range (0, rows):
            temp = matrix[i][n]
            if (i != Xrow):
                for j in range (0, columns):
                    matrix[i][j] = matrix[i][j] - (temp*matrix[Xrow][j])
        print(matrix)
        print()

    '''negative = 0
    #check if max z value row has any negative values
    for n in range (0, columns):
        if (matrix[rows - 1][n] < 0):
            Xrow = n
            negative = 1

    #normalize pivot row if there are negative values
    if (negative == 1):
        temp = matrix[rows - 1][Xrow]
        for i in range (0, columns):
            matrix[rows - 1][i] = matrix[rows - 1][i] - temp

    #row reduction
    for i in range (0, rows):
        temp = matrix[i][Xrow]
        print(temp)
        if (i != (rows - 1)):
            for j in range (0, columns):
                matrix[i][j] = matrix[i][j] - (temp*matrix[rows - 1][j])'''

    print(matrix)
    print()

    zero = 0
    for i in range (0, num):
        for j in range (0, num):
            if (matrix[j][i] == 1):
                print("X{} = {}".format(i, matrix[j][len(matrix[j])-1]))
                zero = 1
        if (zero == 0):
            print("X{} = 0".format(i))
            zero = 1



main()
