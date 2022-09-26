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
# [
#   [5, 3, 4,. 6, 7, 8,. 9, 1, 2],
#   [6, 7, 2,. 1, 9, 5,. 3, 4, 8],
#   [1, 9, 8,. 3, 4, 2,. 5, 6, 7],.
#   [8, 5, 9,. 7, 6, 1,. 4, 2, 3],
#   [4, 2, 6,. 8, 5, 3,. 7, 9, 1],
#   [7, 1, 3,. 9, 2, 4,. 8, 5, 6],.
#   [9, 6, 1,. 5, 3, 7,. 2, 8, 4],
#   [2, 8, 7,. 4, 1, 9,. 6, 3, 5],
#   [3, 4, 5,. 2, 8, 6,. 1, 7, 9]
# ]

# correctGrid1=toAssess.split(.)

toAssess=shouldBeCorrect
new=[]
checkedNum=[]   #number we checked already can't appear again, so if it's checked any more times after the 1st, it's wrong
noZero=[1,2,3,4,5,6,7,8,9]

for row in range(9):  
  for col in range(9):         #row is 0. 
    if toAssess[row][col] in checkedNum:
      print("2 of the same number is in this row")
      break
    elif toAssess[row][col] in noZero:   #if it's not a zero
      checkedNum.append(toAssess[row][col])
      print(checkedNum) # printed 5, from [0][0]
  new.append(checkedNum)
  print(new)
  checkedNum=[]
if new==toAssess:
  print("yes")

# column 1: j is 0; column 2: j is 1; column 3: j is 2;... column 9: j is 8
# column 1: [0->8][0];  column 2: [0->8][1];... column 9: [0->8][8]

#TODO: have not done first half of L31 "has to have 1-9", so do it. First things first
#TODO: do columns next. An idea: switch columns into rows then check those new rows that way
#TODO: for boxes, it may be similar to columns. Whereas with columns, you take 1 element of every list 9 times, with boxes, you take 3 elements for 3 by 3 times

#   print(checkedNum)     # printed 3, from [0][1] or [3][8] or [8][0]?
# print(checkedNum)       # printed 6, from [i?][j?] 

# ******* CLEAR checkedNum every time j GETS TO 8 *******
# ******* REFILL noZero every time j GETS TO 8 *******