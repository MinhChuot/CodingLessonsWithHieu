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

# ***Checking rows***
for row in range(9):  
  for col in range(9):         #row is 0. 
    if toAssess[row][col] in checkedNum:
      print("2 of the same number is in this row")
      break
    elif toAssess[row][col] in noZero:   #if it's not a zero
      checkedNum.append(toAssess[row][col])
      # print(checkedNum) # printed 5, from [0][0]
  new.append(checkedNum)
  # print(new)
  checkedNum=[]
if new==toAssess:
  print("Rows are all valid")
else:
  print("There is/are one or more invalid row/s")

# ***Checking columns***
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
# invertedShouldBeCorrect=[
# [],[],[],[],[],[],[],[],[]
# ]     This is in case I need to append during the loop instead of having it as lines in the script 
for i in range(9):
  for j in range(9):
    if j==0:
      col1.append(toAssess[i][j])
    elif j==1:
      col2.append(toAssess[i][j])
    elif j==2:
      col3.append(toAssess[i][j])
    elif j==3:
      col4.append(toAssess[i][j])
    elif j==4:
      col5.append(toAssess[i][j])
    elif j==5:
      col6.append(toAssess[i][j])
    elif j==6:
      col7.append(toAssess[i][j])
    elif j==7:
      col8.append(toAssess[i][j])
    elif j==8:
      col9.append(toAssess[i][j])
invertedShouldBeCorrect.append(col1)
invertedShouldBeCorrect.append(col2)
invertedShouldBeCorrect.append(col3)
invertedShouldBeCorrect.append(col4)
invertedShouldBeCorrect.append(col5)
invertedShouldBeCorrect.append(col6)
invertedShouldBeCorrect.append(col7)
invertedShouldBeCorrect.append(col8)
invertedShouldBeCorrect.append(col9)

toAssess=invertedShouldBeCorrect
invertedNew=[]

for row in range(9):  
  for col in range(9):         #row is 0. 
    if toAssess[row][col] in checkedNum:
      print("2 of the same number is in this row")
      break
    elif toAssess[row][col] in noZero:   #if it's not a zero
      checkedNum.append(toAssess[row][col])
  # print(checkedNum) # printed 5, from [0][0]
  invertedNew.append(checkedNum)
  checkedNum=[]
# print(invertedNew)

if invertedNew==toAssess:
  print("Columns are all valid")
else:
  print("There is/are one or more invalid column/s")

#TODO: for boxes, it may be similar to columns. Whereas with columns, you take 1 element of every list 9 times, with boxes, you take 3 elements for 3 times and repeat that 8 more times

#   print(checkedNum)     # printed 3, from [0][1] or [3][8] or [8][0]?
# print(checkedNum)       # printed 6, from [i?][j?] 