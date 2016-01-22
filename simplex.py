def main():
    matrix = [[1,2,1,0,40], [4,3,0,1,120], [-40,-50,0,0,0]]
    simplex_algorithm(matrix)

    print()
    matrix = [[1,2,5,1,0,0,40],[4,3,7,0,1,0,120],[5,7,6,0,0,1,150],[-40,-50,-80,0,0,0,0]]
    print()
    simplex_algorithm(matrix)

    print()
    matrix = [[1,2,5,10,1,0,0,0,40],[4,3,7,1,0,1,0,0,120],[5,7,6,2,0,0,1,0,150],[6,1,8,7,0,0,0,1,130],[-40,-50,-80,-200,0,0,0,0,0]]
    simplex_algorithm(matrix)

def simplex_algorithm(matrix):
    #obtain the amount of rows & columns
    rows = len(matrix)
    columns = len(matrix[0])

    #print matrix
    for i in range (0, rows):
        for j in range (0, columns):
            print(matrix[i][j], end="\t")
        print()
    print()
    
    #obtain number of variables
    num = int((columns - 1) - (columns - 1)/2)

    x = []          #this list contains solution vector
    negative = 1
    
    #keep performing simplex algorithm as long as objective row has negative values
    while (negative == 1):
        #check if last row has any negative values
        negative = 0
        for i in range (0, columns):
            if (matrix[rows-1][i] < 0):
                negative = 1

        #if negative values, perform simplex algorithm
        if (negative == 1):
            #find pivot column based on the most negative number
            temp = matrix[rows-1][0]
            pivot_column = 0
            for i in range (1, columns):
                if (temp > matrix[rows-1][i]):
                    temp = matrix[rows-1][i]
                    pivot_column = i

            #find the pivot row
            #b/matrix[row][pivot_column]
            #lowest value, but still positive
            Xmin = 1000000
            for i in range (0, rows-1):
                if (matrix[i][pivot_column] != 0 and matrix[i][pivot_column] > 0):
                    temp = matrix[i][len(matrix[i])-1]/matrix[i][pivot_column]
                    if (Xmin > temp):
                        Xmin = temp
                        pivot_row = i   

            #normalize the pivot row
            temp = matrix[pivot_row][pivot_column]
            for i in range (0, columns):
                matrix[pivot_row][i] = matrix[pivot_row][i]/temp

            #row reduction operation
            for i in range (0, rows):
                temp = matrix[i][pivot_column]
                if (i != pivot_row):
                    for j in range (0, columns):
                        matrix[i][j] = matrix[i][j] - (temp*matrix[pivot_row][j])

            for i in range (0, rows):
                for j in range (0, columns):
                    print("{0:.2f}".format(matrix[i][j]), end="\t")
                print()
            print()

    for i in range (0, num):
        zero = 0
        one = 0
        for j in range (0, num):
            if (matrix[j][i] == 1):
                if (one == 1):
                    zero = 1
                else:            
                    one = 1
                    index = j
                    
        if (zero == 1 or one == 0):
            print("X{} = 0".format(i))
            x.append(0)
        else:
            print("X{} = {}".format(i, matrix[index][len(matrix[index])-1]))
            x.append(matrix[index][len(matrix[index])-1])

    print("F = ", matrix[rows-1][columns-1])
    #print(x)
            
main()
