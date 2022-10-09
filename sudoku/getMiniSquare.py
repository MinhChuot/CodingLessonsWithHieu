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
  if squareNum==1:   #if i+1==1, a.k.a. i==0
    for row in range(squareNum-squareNum,3*squareNum): # (squareNum-1, squareNum+2)-> same as 4's row
      for col in range(squareNum-squareNum, 3*squareNum): # (squareNum-1, squareNum+2)
        out.append(grid[row][col])
    print(out)
    return out
  if squareNum==2:  #if i+1==2, a.k.a. i==1
    for row in range(squareNum-squareNum,squareNum+1): # (squareNum-2, squareNum+1)-> same as 5's row 
      for col in range(squareNum+1, 3*squareNum):      # (squareNum+1, squareNum+4)
        out.append(grid[row][col])
    print(out)
    return out
  if squareNum==3:  #if i+1==3, a.k.a. i==2
    for row in range(squareNum-3,squareNum):  # same as 6's row ->(squareNum-squareNum, squareNum) 
      for col in range(2*squareNum, 3*squareNum):     # (squareNum+3, squareNum+6)
        out.append(grid[row][col])
    print(out)
    return out
  if squareNum==4:  #if i+1==4, a.k.a. i==3
    for row in range(squareNum-1,squareNum+2):            
      for col in range(squareNum-squareNum, squareNum-1): 
        out.append(grid[row][col])
    print(out)
    return out
  if squareNum==5:  #if i+1==5, a.k.a. i==4
    for row in range(squareNum-2,squareNum+1):            
      for col in range(squareNum-2, squareNum+1): 
        out.append(grid[row][col])
    print(out)
    return out
  if squareNum==6:  #if i+1==6, a.k.a. i==5
    for row in range(squareNum-3,squareNum):            
      for col in range(squareNum, squareNum+3): 
        out.append(grid[row][col])
    print(out)
    return out
  if squareNum==7:  #if i+1==7, a.k.a. i==6
    for row in range(squareNum-1,squareNum+2):            
      for col in range(squareNum-squareNum, squareNum-4): 
        out.append(grid[row][col])
    print(out)
    return out
  if squareNum==8:  #if i+1==8, a.k.a. i==7
    for row in range(squareNum-2,squareNum+1):            
      for col in range(squareNum-5, squareNum-2): 
        out.append(grid[row][col])
    print(out)
    return out
  if squareNum==9:  #if i+1==9, a.k.a. i==8
    for row in range(squareNum-3,squareNum):            
      for col in range(squareNum-3, squareNum): 
        out.append(grid[row][col])
    print(out)
    return out


# x=getMiniSquare(1, toAssess)
# print(x)

newGrid=[]
for i in range(9):
  # x=[]
  x=getMiniSquare(i+1, toAssess) #call/run the function AND get out[] into x in 1 step
  newGrid.append(x)
print(newGrid)
print(x)


# squareNum = 1, i:0->2 (0,3) & j:0->2 (0,3)
# squareNum = 2, i:0->2 (0,3) & j:3->5 (3,6)
# squareNum = 3, i:0->2 (0,3) & j:6->8 (6,9)

# squareNum = 4, i:3->5 (3,6) & j:0->2 (0,3)
# squareNum = 5, i:3->5 (3,6) & j:3->5 (3,6)
# squareNum = 6, i:3->5 (3,6) & j:6->8 (6,9)

# squareNum = 7, i:6->8 (6,9) & j:0->2 (0,3)
# squareNum = 8, i:6->8 (6,9) & j:3->5 (3,6)
# squareNum = 9, i:6->8 (6,9) & j:6->8 (6,9)