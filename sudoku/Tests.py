# test=[["5", "3", "4", "6", "7", "8", "9", "1", "2"],
# ["6", "7", "2", "1", "9", "5", "3", "4", "8"]]
# toAssess=test
# # toAssess=shouldBeCorrect
# checkedNum=[]   #number we checked already can't appear again, so if it's checked any more times after the 1st, it's wrong
# # uncheckedNum=[1,2,3,4,5,6,7,8,9]
# uncheckedNum=["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# for i in range(len(toAssess)):              # "for 9 times, and i goes 0 to 8"
#   for j in range(len(toAssess[i])):         #i is 0. "for 9 times, j goes 0 to 8" 
#     if toAssess[i][j] in checkedNum:  #TypeError: argument of type 'int' is not iterable
#       print("2 of the same number is in this row")
#     elif toAssess[i][j] in uncheckedNum:      #j is 0, 'if this number is anywhere 1-9'.  [0][0] is 5, so toAssess[i][j] is 5 for now. 
#       checkedNum.append(toAssess[i][j])
#       # uncheckedNum.pop(toAssess[i][j]-1)   #if 5 (aka.toAssess[i][j]) is in uncheckedNum then it is at position unCheckedNum[5-1]   
# #     IndexError: pop index out of range
#       print(checkedNum) # printed 5, from [0][0]
#       print(uncheckedNum)

# Output: 
# ['5']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['5', '3']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['5', '3', '4']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['5', '3', '4', '6']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['5', '3', '4', '6', '7']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['5', '3', '4', '6', '7', '8']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['5', '3', '4', '6', '7', '8', '9']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['5', '3', '4', '6', '7', '8', '9', '1']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['5', '3', '4', '6', '7', '8', '9', '1', '2']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# 2 of the same number is in this row
# 2 of the same number is in this row
# 2 of the same number is in this row
# 2 of the same number is in this row
# 2 of the same number is in this row
# 2 of the same number is in this row
# 2 of the same number is in this row
# 2 of the same number is in this row
# 2 of the same number is in this row
#################################################################
# for row in range(9):  
#   for col in range(9):         #row is 0. 
#     if toAssess[row][col] in checkedNum:  
#       print("2 of the same number is in this row")
#     elif toAssess[row][col] in uncheckedNum:    #why is uncheckedNum still here?
#       print(toAssess[row][col])
#       checkedNum.append(toAssess[row][col])
#       uncheckedNum.pop(toAssess[row][col]-1)
# #     IndexError: pop index out of range
#       print(checkedNum) # printed 5, from [0][0]
#       print(uncheckedNum)
#   checkedNum=[]

# Output:  
# $ python sudoku/main.py
# 5
# [5]
# [1, 2, 3, 4, 6, 7, 8, 9]
# 3
# [5, 3]
# [1, 2, 4, 6, 7, 8, 9]
# 4
# [5, 3, 4]
# [1, 2, 4, 7, 8, 9]

######################################################################################
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
toAssess=shouldBeCorrect
####################
# checkedNum=[]   #number we checked already can't appear again, so if it's checked any more times after the 1st, it's wrong
# noZero=[1,2,3,4,5,6,7,8,9]
new=[]

#***********Checking Rows***************** 
def checkRows(tA):
  checkedNum=[]
  noZero=[1,2,3,4,5,6,7,8,9]
  new=[]
  # print(checkedNum)
  for row in range(9):  
    for col in range(9):         #row is 0. 
      # if tA[row][col] == 0:
      #   print("The digit is not an integer from 1 to 9, and so it is invalid")
      # print(tA[row][col])
      # print(checkedNum)
      # print(noZero)
      if tA[row][col] in checkedNum:
        print("2 of the same number is in this row")
        break
      elif tA[row][col] in noZero:   #if it's not a zero
        checkedNum.append(tA[row][col])
        # print(checkedNum) # printed 5, from [0][0]
    new.append(checkedNum)
    # print(new) #once every "9 times" for 9 times
    checkedNum=[]
  if new==toAssess:
    print("Rows are all valid")
  else:
    print("There is/are one or more invalid row/s")
    # return new

# def feedback(new):
  # if new==toAssess:
  #   print("Rows are all valid")
  # else:
  #   print("There is/are one or more invalid row/s")

checkRows(toAssess)

# feedback(new) #this new is empty
# Presentable Output:
# There is/are one or more invalid row/s
# the new[] in feedback(new) is empty and NOT THE SAME new[] is inside checkRows(). THEREFORE,
# newGrid takes the empty new[] outside checkRows() instead of the new[] inside it

# checkRows(shouldBeCorrect)
# checkRows(shouldBeIncorrect)


# for row in range(9):  
#   for col in range(9):         #row is 0. 
#     # if toAssess[row][col] == 0:
#     #   print("The digit is not an integer from 1 to 9, and so it is invalid")
#     if toAssess[row][col] in checkedNum:
#       print("2 of the same number is in this row")
#       break
#     elif toAssess[row][col] in noZero:   #if it's not a zero
#       checkedNum.append(toAssess[row][col])
#       # print(checkedNum) # printed 5, from [0][0]
#   new.append(checkedNum)
#   # print(new)
#   checkedNum=[]
#   if new==toAssess:
#     print("Rows are all valid")
#   else:
#     print("There is/are one or more invalid row/s")

# exit(1) #dont forget about this


# ************************************Checking columns*********************************
invertedShouldBeCorrect=[]
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]
col8=[]
col9=[]

# invertedShouldBeCorrect=[
# [],[],[],[],[],[],[],[],[]
# ]     This is in case I need to append during the loop instead of having it as lines in the script 

for i in range(9):  #************ Find a way to REUSE col1[]***************
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

# print(col1)
# print(col2)
# print(col3)
# print(col4)
# print(col5)
# print(col6)
# print(col7)
# print(col8)
# print(col9)

# 1st try at simplifying things for checking columns
#  for i in range(9):  #************ Find a way to REUSE col1[]***************
#   for j in range(9):
#     if j==0:
#       col1.append(toAssess[i][j])
#       invertedShouldBeCorrect.append(col1)
#   print(col1)
#   print(invertedShouldBeCorrect)
#     elif j==1:
#       col1.append(toAssess[i][j])
#     elif j==2:
#       col1.append(toAssess[i][j])

invertedShouldBeCorrect.append(col1)
invertedShouldBeCorrect.append(col2)
invertedShouldBeCorrect.append(col3)
invertedShouldBeCorrect.append(col4)
invertedShouldBeCorrect.append(col5)
invertedShouldBeCorrect.append(col6)
invertedShouldBeCorrect.append(col7)
invertedShouldBeCorrect.append(col8)
invertedShouldBeCorrect.append(col9)

# print(invertedShouldBeCorrect)
# Output:
# [
# [5, 6, 1, 8, 4, 7, 9, 2, 3],
# [3, 7, 9, 5, 2, 1, 6, 8, 4],
# [4, 2, 8, 9, 6, 3, 1, 7, 5], 
# [6, 1, 3, 7, 8, 9, 5, 4, 2], 
# [7, 9, 4, 6, 5, 2, 3, 1, 8], 
# [8, 5, 2, 1, 3, 4, 7, 9, 6], 
# [9, 3, 5, 4, 7, 8, 2, 6, 1], 
# [1, 4, 6, 2, 9, 5, 8, 3, 7], 
# [2, 8, 7, 3, 1, 6, 4, 5, 9]
# ]

toAssess=invertedShouldBeCorrect

# invertedNew=[]

# for row in range(9):  
#   for col in range(9):         #row is 0. 
#     # if toAssess[row][col] == 0:
#     #   print("The digit is not an integer from 1 to 9, and so it is invalid")
#     if toAssess[row][col] in checkedNum:
#       print("2 of the same number is in this row")
#       break
#     elif toAssess[row][col] in noZero:   #if it's not a zero
#       checkedNum.append(toAssess[row][col])
#   # print(checkedNum) # printed 5, from [0][0]
#   invertedNew.append(checkedNum)
#   checkedNum=[]
# print(invertedNew)

# if invertedNew==toAssess:
#   print("Columns are all valid")
# else:
#   print("There is/are one or more invalid column/s")


# checkRows(invertedShouldBeCorrect)
checkRows(toAssess)

# ******************************************Checking Boxes****************************************
# for i in range(9):
#   for j in range(9):
#     if j==0:
#       col.append(toAssess[i][j])
#       print(col) ********************
#     elif j==1:
#       col2.append(toAssess[i][j])
#       print(col2)  *******************
# Output:   Below might help with invertedShouldBeCorrect=[ [],[],[],[],[],[],[],[],[] ] 
# [5]
# [3]
# [5, 6]
# [3, 7]
# [5, 6, 1]
# [3, 7, 9]
# [5, 6, 1, 8]
# [3, 7, 9, 5]
# [5, 6, 1, 8, 4]
# [3, 7, 9, 5, 2]
# [5, 6, 1, 8, 4, 7]
# [3, 7, 9, 5, 2, 1]
# [5, 6, 1, 8, 4, 7, 9]
# [3, 7, 9, 5, 2, 1, 6]
# [5, 6, 1, 8, 4, 7, 9, 2]
# [3, 7, 9, 5, 2, 1, 6, 8]
# [5, 6, 1, 8, 4, 7, 9, 2, 3]
# [3, 7, 9, 5, 2, 1, 6, 8, 4]

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
boxesShouldBeCorrect=[]
# j=0

def threeByNine(pop, j):  
  for i in range(9):  
    for j in range(9):
      if j<=2:
        pop1.append(toAssess[i][j])

# Output:
# [5]
# [5, 3]
# [5, 3, 4]
# [5, 3, 4, 6]
# [5, 3, 4, 6, 7]
# [5, 3, 4, 6, 7, 2]
# [5, 3, 4, 6, 7, 2, 1]
# [5, 3, 4, 6, 7, 2, 1, 9]
# [5, 3, 4, 6, 7, 2, 1, 9, 8] #Up to here alone should be BIG HINT to the SOLUTION for CHECKING BOXES
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1, 2]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1, 2, 8]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1, 2, 8, 7]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1, 2, 8, 7, 3]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1, 2, 8, 7, 3, 4]
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1, 2, 8, 7, 3, 4, 5]

#3rd try at checking boxes
# for k in range(3):
#   for m in range(9):
#     if len(pop1)>18:
#       box1=pop1.pop(pop1[m])
#     elif len(pop1)>9:
#       box2=pop1.pop(pop1[m])
#     # elif len(pop1)<=9:
#     #   box3=pop1.pop(pop1[m])
# print(box1)
# print(box2)
# print(box3)
# [5, 3, 4, 6, 7, 2, 1, 9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1, 2, 8, 7, 3, 4, 5]
# Output:
# [5, 3, 4,    7,       9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1, 2, 8, 7, 3, 4, 5]
# [5, 3, 4,    7,       9, 8, 8, 5, 9, 4, 2, 6, 7, 1, 3, 9, 6, 1, 2, 8, 7, 3, 4, 5]

#5th try at checking boxes
# for k in range(3):    #3 for pop1, pop2, pop3
#   for m in range(9):  #9 so each of pop1, pop2, pop3 gets 9
#     if len(pop1)>18:  #starts at length=27, appends and pops first 9 to pop1. then, next 9 to pop2, etc.
#       box1.append(pop1[m])
#       pop1.pop()
#     elif len(pop1)>9: #now length=18, "first" 9 to pop2
#       box2.append(pop1[m+9])
#     elif len(pop1)<=9:  #now length=9, "first" 9 to pop3
#       box3.append(pop1[m+18])
# print(box1)
# print(box2)
# print(box3)

#6th try at checking boxes: trying to not require pop method
# def getMiniSquares():
for k in range(3):    #3 for pop1, pop2, pop3
  for m in range(9):  #9 so each of pop1, pop2, pop3 gets 9
    if len(box1)<9:  #
      box1.append(pop1[m])
    elif len(box1)==9 and len(box2)<9: #
      box2.append(pop1[m+9])
    elif len(box2)==9 and len(box3)<9:  #
      box3.append(pop1[m+18])
  # boxesShouldBeCorrect.append(box1)
  # boxesShouldBeCorrect.append(box2)
  # boxesShouldBeCorrect.append(box3)
  # box1=[]
  # box2=[]
  # box3=[]
# print(box1)
# print(box2)
# print(box3)

#4th try at checking boxes
# for m in range(9):
#   box1.append(pop1[m])
#   pop1.pop(pop1[m])
#   print(box1)
# print(pop1)
# OUtput:
# [5]
# [5, 3]
# [5, 3, 4]
# [5, 3, 4, 7]
# [5, 3, 4, 7, 9]
# [5, 3, 4, 7, 9, 8]
# [5, 3, 4, 7, 9, 8, 8]
# [5, 3, 4, 7, 9, 8, 8, 9]
# [5, 3, 4, 7, 9, 8, 8, 9, 7]
# [5, 3, 4, 7, 9, 8, 8, 7, 3, 9, 6, 1, 2, 8, 7, 3, 4, 5]

# Divide Line above into 3 groups of 9 then:

for i in range(9):  
  for j in range(9):
    if j>2 or j<=5:
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
# print(box4)
# print(box5)
# print(box6)
 
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
# print(box7)
# print(box8)
# print(box9)

boxesShouldBeCorrect.append(box1)
boxesShouldBeCorrect.append(box2)
boxesShouldBeCorrect.append(box3)
boxesShouldBeCorrect.append(box4)
boxesShouldBeCorrect.append(box5)
boxesShouldBeCorrect.append(box6)
boxesShouldBeCorrect.append(box7)
boxesShouldBeCorrect.append(box8)
boxesShouldBeCorrect.append(box9)
# print(boxesShouldBeCorrect)
# Output:
# [[5, 3, 4, 6, 7, 2, 1, 9, 8], 
# [8, 5, 9, 4, 2, 6, 7, 1, 3], 
# [9, 6 1, 2, 8, 7, 3, 4, 5], 
# [6, 7, 8, 1, 9, 5, 3, 4, 2], 
# [7, 6, 1, 8,5, 3, 9, 2, 4], 
# [5, 3, 7, 4, 1, 9, 2, 8, 6], 
# [9, 1, 2, 3, 4, 8, , 6, 7], 
# [4, 2, 3, 7, 9, 1, 8, 5, 6], 
# [2, 8, 4, 6, 3, 5, 1, 7, 9]]

toAssess=boxesShouldBeCorrect
# boxesNew=[]
# checkRows(boxesShouldBeCorrect)
checkRows(toAssess)
# for row in range(9):  
#   for col in range(9):         #row is 0. 
#     # if toAssess[row][col] == 0:
#     #   print("The digit is not an integer from 1 to 9, and so it is invalid")
#     if toAssess[row][col] in checkedNum:
#       print("2 of the same number is in this row")
#       break
#     elif toAssess[row][col] in noZero:   #if it's not a zero
#       checkedNum.append(toAssess[row][col])
#   # print(checkedNum) # printed 5, from [0][0]
#   boxesNew.append(checkedNum)
#   checkedNum=[]
# print(invertedNew)

# if boxesNew==toAssess:
#   print("Mini-squares are all valid")
# else:
#   print("There is/are one or more invalid mini-square/s")