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

# ***Checking columns***
# column 1: j is 0; column 2: j is 1; column 3: j is 2;... column 9: j is 8
# column 1: [0->8][0];  column 2: [0->8][1];... column 9: [0->8][8]

#TODO: do columns next. An idea: switch columns into rows then check those new rows that way
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
# print(col1)
# print(col2)
# print(col3)
# print(col4)
# print(col5)
# print(col6)
# print(col7)
# print(col8)
# print(col9)
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
# print(toAssess)
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

# for i in range(9):
#   for j in range(9):
#     if j==0:
#       col1.append(toAssess[i][j])
#       print(col1) ********************
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