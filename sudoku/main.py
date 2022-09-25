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
#	- numbers can't be in same column/row/box, e.g. # something in [0][0] can't be in [0][j] nor in [i][0]
#	- has to have 1-9, NOT ZERO, without repeating any number

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
checkedNum=[]   #number we checked already can't appear again, so if it's checked any more times after the 1st, it's wrong
uncheckedNum=[1,2,3,4,5,6,7,8,9]

for i in range(len(toAssess)):              # "for 9 times, and i goes 0 to 8"
  for j in range(len(toAssess[i])):         #i is 0. "for 9 times, j goes 0 to 8" 
    if toAssess[i][j] in checkedNum:  #TypeError: argument of type 'int' is not iterable
      print("2 of the same number is in this row")
    elif toAssess[i][j] in uncheckedNum:      #j is 0, 'if this number is anywhere 1-9'.  [0][0] is 5, so toAssess[i][j] is 5 for now. 
      checkedNum=uncheckedNum.pop(toAssess[i][j]-1)   #if 5 (aka.toAssess[i][j]) is in uncheckedNum then it is at position unCheckedNum[5-1]   
#     IndexError: pop index out of range
      print(checkedNum) # printed 5, from [0][0]
      print(uncheckedNum)

# only popped once for first number, ie [0][0]. 
# 5
# [1, 2, 3, 4, 6, 7, 8, 9]
# because TypeError on line 54

#   print(checkedNum)     # printed 3, from [0][1] or [3][8] or [8][0]?
# print(checkedNum)       # printed 6, from [i?][j?]

# ******* CLEAR checkedNum every time j GETS TO 8 *******
# ******* REFILL uncheckedNum every time j GETS TO 8 *******
#########################################################################################
# numberBox=[]
# for a in range(9):
#   numberBox.append(a+1) #forgetting the objective and thinking we have to reproduce the lists
# popping and catching may help