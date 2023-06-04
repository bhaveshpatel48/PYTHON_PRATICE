'''
#~> Notes:
    #$ In the wrong way, Inner list object is created once and same reference is being used by all elements of outer list
    #$ Ex : lst = [  [0]*cols ] * rows 
            lst -> piunts to reference 232839238
            lst[0] -> pints to reference 12134354
            lst[1] -> pints to reference 12134354
            .
            .
            .
            lst[rows-1] -> pints to reference 12134354
    #$ Because of the above way of creation of matrix under the hood in python, we face the issue of updating cells in matrix
'''

rows = 2
cols = 2

#~! Wrong way
matrix = [[0]*cols ] * rows     #? There is one problem here...
print(" initial Matrix : ", matrix)
matrix[0][1] = 1    #? This will update every row's col-1 position of matrix to 1
print(" final Matrix : ", matrix)

#~^ Correct way
matrix = [[0]*cols for _ in range(rows)]
print("\nCorrect way of doing...")
print("\tinitial Matrix : ", matrix)
matrix[0][1] = 1
print("\tfinal Matrix : ", matrix)