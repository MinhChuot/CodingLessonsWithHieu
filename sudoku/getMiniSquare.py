toAssess=[
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

# [
# [5, 3, 4, 6, 7, 2, 1, 9, 8], 
# [6, 7, 8, 1, 9, 5, 3, 4, 2], 
# [9, 1, 2, 3, 4, 8, 5, 6, 7], 
# [8, 5, 9, 4, 2, 6, 7, 1, 3], 
# [7, 6, 1, 8, 5, 3, 9, 2, 4], 
# [4, 2, 3, 7, 9, 1, 8, 5, 6], 
# [9, 6, 1, 2, 8, 7, 3, 4, 5], 
# [5, 3, 7, 4, 1, 9, 2, 8, 6], 
# [2, 8, 4, 6, 3, 5, 1, 7, 9]
# ]

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

# squareNum = 1, i:0->2 (0,3) & j:0->2 (0,3)
# squareNum = 2, i:0->2 (0,3) & j:3->5 (3,6)
# squareNum = 3, i:0->2 (0,3) & j:6->8 (6,9)

# squareNum = 4, i:3->5 (3,6) & j:0->2 (0,3)
# squareNum = 5, i:3->5 (3,6) & j:3->5 (3,6)
# squareNum = 6, i:3->5 (3,6) & j:6->8 (6,9)

# squareNum = 7, i:6->8 (6,9) & j:0->2 (0,3)
# squareNum = 8, i:6->8 (6,9) & j:3->5 (3,6)
# squareNum = 9, i:6->8 (6,9) & j:6->8 (6,9)