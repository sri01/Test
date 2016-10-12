# List comprehension
# prints a 3 x 3 matrix as list of lists.
# diagonal elements are 1, rest are 0
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]

def withoutListComp():
    mym = []
    mat = []

    for i in 0,1,2:
        for j in 0,1,2:
            if i == j:
                mym.append(1)
            else:
                mym.append(0)
            #print(mym)
        mat.append(mym)
        #print("Outer list: ")
        #print(mat)
        mym=[]

    print(mat)

withoutListComp()

def listComp():


    # [value_when_condition_is_true for value in InputValues if condition]

   print([ [1 if r == c else 0 for r in range(0,3)] for c in range(0,3) ] )



listComp()



