shouldBeCorrect=[
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
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
# - numbers can't be in same column/row/box, e.g. # something in [0][0] can't be in [0][j] nor in [i][0]
# - has to have 1-9, NOT ZERO, without repeating any number

######################################################################################################################

#*******************************Checking Rows************************************ 
toAssess=shouldBeCorrect
# toAssess=shouldBeIncorrect

def checkRows(tA):
  checkedNum=[]
  noZero=[1,2,3,4,5,6,7,8,9]
  new=[]
  for row in range(9):  
    for col in range(9):          
      if tA[row][col] in checkedNum:
        print("No") #2 of the same number is in this row
        break
      elif tA[row][col] in noZero:   
        checkedNum.append(tA[row][col])
    new.append(checkedNum)
    checkedNum=[]
  if new==tA: 
    print("Yes") #Rows are all valid
  else:
    print("No") #There is/are one or more invalid row/column/mini-square/s

checkRows(toAssess)

# *******************************Checking columns****************************************
invertedShouldBeCorrect=[
[],[],[],[],[],[],[],[],[]
]

for row in range(9):
  for col in range(9):
    invertedShouldBeCorrect[col].append(toAssess[row][col])

checkRows(invertedShouldBeCorrect)

# ********************************** Checking boxes *********************************
toAssess=shouldBeCorrect
def getMiniSquare(squareNum, grid):
  out=[]
  if squareNum in (1,2,3):     
    rowStart=0
    rowEnd=3
  elif squareNum in (4,5,6):
    rowStart=3
    rowEnd=6
  elif squareNum in (7,8,9):
    rowStart=6
    rowEnd=9
  if squareNum in (1,4,7):
    colStart=0
    colEnd=3
  if squareNum in (2,5,8):
    colStart=3
    colEnd=6 
  if squareNum in (3,6,9):
    colStart=6
    colEnd=9 

  for row in range(rowStart,rowEnd):
    for col in range(colStart,colEnd): 
      out.append(grid[row][col])
  return out

newGrid=[]
for i in range(9):
  x=getMiniSquare(i+1, toAssess) #call/run the function AND get out[] into x in 1 step
  newGrid.append(x)

checkRows(toAssess)