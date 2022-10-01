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

#***********Checking Rows***************** 
toAssess=shouldBeCorrect
new=[]
checkedNum=[]   #number we checked already can't appear again, so if it's checked any more times after the 1st, it's wrong
noZero=[1,2,3,4,5,6,7,8,9]

# ***Checking rows***
for row in range(9):  
  for col in range(9):         #row is 0. 
    if toAssess[row][col] == 0:
      print("The digit is not an integer from 1 to 9, and so it is invalid")
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

# ***Checking columns*** #is there a way to/is it necessary to automate more of the code below with loops?
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

toAssess=invertedShouldBeCorrect
invertedNew=[]

for row in range(9):  
  for col in range(9):         #row is 0. 
    if toAssess[row][col] == 0:
      print("The digit is not an integer from 1 to 9, and so it is invalid")
    if toAssess[row][col] in checkedNum:
      print("2 of the same number is in this row")
      break
    elif toAssess[row][col] in noZero:   #if it's not a zero
      checkedNum.append(toAssess[row][col])
  invertedNew.append(checkedNum)
  checkedNum=[]

if invertedNew==toAssess:
  print("Columns are all valid")
else:
  print("There is/are one or more invalid column/s")

#TODO: for boxes, it may be similar to columns. Whereas with columns, you take 1 element of every list 9 times, with boxes, you take 3 elements for 3 times and repeat that 8 more times
# ********* Checking boxes **********
pop1=[]
pop2=[]
pop3=[]

box1=[]
box2=[]
box3=[]
box4=[]
box5=[]
box6=[]
box7=[]
box8=[]
box9=[]

for i in range(9):  
  for j in range(9):
    if j==0:
      pop1.append(toAssess[i][j])
    elif j==1:
      pop1.append(toAssess[i][j])
    elif j==2:
      pop1.append(toAssess[i][j])

#trying to not require pop method
for k in range(3):    #3 for pop1, pop2, pop3
  for m in range(9):  #9 so each of pop1, pop2, pop3 gets 9
    if len(box1)<9:  #
      box1.append(pop1[m])
    elif len(box1)==9 and len(box2)<9: #
      box2.append(pop1[m+9])
    elif len(box2)==9 and len(box3)<9:  #
      box3.append(pop1[m+18])

for i in range(9):  
  for j in range(9):
    if j==3:
      pop2.append(toAssess[i][j])
    elif j==4:
      pop2.append(toAssess[i][j])
    elif j==5:
      pop2.append(toAssess[i][j])
# print(pop2)
# Output
# [6, 7, 8, 1, 9, 5, 3, 4, 2, 7, 6, 1, 8, 5, 3, 9, 2, 4, 5, 3, 7, 4, 1, 9, 2, 8, 6]

for k in range(3):    #3 for pop2, pop2, pop3
  for m in range(9):  #9 so each of pop2, pop2, pop3 gets 9
    if len(box4)<9:  #
      box4.append(pop2[m])
    elif len(box4)==9 and len(box5)<9: #
      box5.append(pop2[m+9])
    elif len(box5)==9 and len(box6)<9:  #
      box6.append(pop2[m+18])

for i in range(9):  
  for j in range(9):
    if j==6:
      pop3.append(toAssess[i][j])
    elif j==7:
      pop3.append(toAssess[i][j])
    elif j==8:
      pop3.append(toAssess[i][j])
# print(pop3)
# Output:
# [9, 1, 2, 3, 4, 8, 5, 6, 7, 4, 2, 3, 7, 9, 1, 8, 5, 6, 2, 8, 4, 6, 3, 5, 1, 7, 9]

for k in range(3):    #3 for pop3, pop2, pop3
  for m in range(9):  #9 so each of pop3, pop2, pop3 gets 9
    if len(box7)<9:  #
      box7.append(pop3[m])
    elif len(box7)==9 and len(box8)<9: #
      box8.append(pop3[m+9])
    elif len(box8)==9 and len(box9)<9:  #
      box9.append(pop3[m+18])

boxesShouldBeCorrect=[]
boxesShouldBeCorrect.append(box1)
boxesShouldBeCorrect.append(box2)
boxesShouldBeCorrect.append(box3)
boxesShouldBeCorrect.append(box4)
boxesShouldBeCorrect.append(box5)
boxesShouldBeCorrect.append(box6)
boxesShouldBeCorrect.append(box7)
boxesShouldBeCorrect.append(box8)
boxesShouldBeCorrect.append(box9)

toAssess=boxesShouldBeCorrect
boxesNew=[]

for row in range(9):  
  for col in range(9):         #row is 0. 
    if toAssess[row][col] == 0:
      print("The digit is not an integer from 1 to 9, and so it is invalid")
    if toAssess[row][col] in checkedNum:
      print("2 of the same number is in this row")
      break
    elif toAssess[row][col] in noZero:   #if it's not a zero
      checkedNum.append(toAssess[row][col])
  # print(checkedNum) # printed 5, from [0][0]
  boxesNew.append(checkedNum)
  checkedNum=[]
# print(invertedNew)

if boxesNew==toAssess:
  print("Mini-squares are all valid")
else:
  print("There is/are one or more invalid mini-square/s")