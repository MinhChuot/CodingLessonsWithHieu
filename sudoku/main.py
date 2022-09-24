shouldBeCorrect=[
  [5, 3, 4,. 6, 7, 8,. 9, 1, 2],
  [6, 7, 2,. 1, 9, 5,. 3, 4, 8],
  [1, 9, 8,. 3, 4, 2,. 5, 6, 7],.
  [8, 5, 9,. 7, 6, 1,. 4, 2, 3],
  [4, 2, 6,. 8, 5, 3,. 7, 9, 1],
  [7, 1, 3,. 9, 2, 4,. 8, 5, 6],.
  [9, 6, 1,. 5, 3, 7,. 2, 8, 4],
  [2, 8, 7,. 4, 1, 9,. 6, 3, 5],
  [3, 4, 5,. 2, 8, 6,. 1, 7, 9]
]
shouldBeIncorrect=[
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]
#write code that will print 'yes' or 'no' depending on whether the sudoku grid is valid.

#shouldBeCorrect-> 'yes'
#shouldBeIncorrect->'no'

#rules of sudoku:
#	- numbers can't be in same column/row/box
#	- has to have 1-9, NOT ZERO, without repeating any number

######################################################################################################################

toAssess=shouldBeCorrect
checkedNum=[]
uncheckedNum=[1,2,3,4,5,6,7,8,9]

for i in range(len(shouldBeCorrect)): # "for 9 times and i goes 0 to 8"
  for j in range(len(shouldBeCorrect[i])): #i is 0. "for 9 times, j goes 0 to 8" 
    #if shouldBeCorrect[i][j] IS NOT in checkedNum:
    #   do 3rd line below, which should be "under" the above if-statement
    # else:
    #   print("2 of the same number is in this row")
    if shouldBeCorrect[i][j] in uncheckedNum: #j is 0, [0][0] is 5. 'if this number is 1-9'
      checkedNum=uncheckedNum.pop(shouldBeCorrect[i][j]-1)


correctGrid1=shouldBeCorrect.split(.)

#something in [0][0] can't be in [0][j] nor in [i][0]

# numberBox=[]
# for a in range(9):
#   numberBox.append(a+1) #forgetting the objective and thinking we have to reproduce the lists
# popping and catching may help

# shouldBeCorrect[0][0]==5
# shouldBeCorrect[8][8]==9


#don't forget to gitpush