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
  if new==toAssess:
    print("Yes") #Rows are all valid
  else:
    print("No") #There is/are one or more invalid row/column/mini-square/s

checkRows(toAssess)

# *******************************Checking columns****************************************
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]
col8=[]
col9=[]
invertedShouldBeCorrect=[]

for row in range(9):
  for col in range(9):
    if col==0:
      col1.append(toAssess[row][col])
    elif col==1:
      col2.append(toAssess[row][col])
    elif col==2:
      col3.append(toAssess[row][col])
    elif col==3:
      col4.append(toAssess[row][col])
    elif col==4:
      col5.append(toAssess[row][col])
    elif col==5:
      col6.append(toAssess[row][col])
    elif col==6:
      col7.append(toAssess[row][col])
    elif col==7:
      col8.append(toAssess[row][col])
    elif col==8:
      col9.append(toAssess[row][col])
invertedShouldBeCorrect.append(col1)
invertedShouldBeCorrect.append(col2)
invertedShouldBeCorrect.append(col3)
invertedShouldBeCorrect.append(col4)
invertedShouldBeCorrect.append(col5)
invertedShouldBeCorrect.append(col6)
invertedShouldBeCorrect.append(col7)
invertedShouldBeCorrect.append(col8)
invertedShouldBeCorrect.append(col9)

checkRows(invertedShouldBeCorrect)

# ********************************** Checking boxes *********************************
def getMiniSquare(squareNum, grid):
  out=[]
  if squareNum==1:   #if i+1==1, a.k.a. i==0
    for row in range(squareNum-squareNum,3*squareNum): 
      for col in range(squareNum-squareNum, 3*squareNum): 
        out.append(grid[row][col])
    return out
  if squareNum==2:  #if i+1==2, a.k.a. i==1
    for row in range(squareNum-squareNum,squareNum+1):  
      for col in range(squareNum+1, 3*squareNum):      
        out.append(grid[row][col])
    return out
  if squareNum==3:  #if i+1==3, a.k.a. i==2
    for row in range(squareNum-3,squareNum):  
      for col in range(2*squareNum, 3*squareNum):     
        out.append(grid[row][col])
    return out
  if squareNum==4:  #if i+1==4, a.k.a. i==3
    for row in range(squareNum-1,squareNum+2):            
      for col in range(squareNum-squareNum, squareNum-1): 
        out.append(grid[row][col])
    return out
  if squareNum==5:  #if i+1==5, a.k.a. i==4
    for row in range(squareNum-2,squareNum+1):            
      for col in range(squareNum-2, squareNum+1): 
        out.append(grid[row][col])
    return out
  if squareNum==6:  #if i+1==6, a.k.a. i==5
    for row in range(squareNum-3,squareNum):            
      for col in range(squareNum, squareNum+3): 
        out.append(grid[row][col])
    return out
  if squareNum==7:  #if i+1==7, a.k.a. i==6
    for row in range(squareNum-1,squareNum+2):            
      for col in range(squareNum-squareNum, squareNum-4): 
        out.append(grid[row][col])
    return out
  if squareNum==8:  #if i+1==8, a.k.a. i==7
    for row in range(squareNum-2,squareNum+1):            
      for col in range(squareNum-5, squareNum-2): 
        out.append(grid[row][col])
    return out
  if squareNum==9:  #if i+1==9, a.k.a. i==8
    for row in range(squareNum-3,squareNum):            
      for col in range(squareNum-3, squareNum): 
        out.append(grid[row][col])
    return out

newGrid=[]
for i in range(9):
  x=getMiniSquare(i+1, toAssess) #call/run the function AND get out[] into x in 1 step
  newGrid.append(x)

checkRows(toAssess)