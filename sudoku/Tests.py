test=[["5", "3", "4", "6", "7", "8", "9", "1", "2"],
["6", "7", "2", "1", "9", "5", "3", "4", "8"]]
toAssess=test
# toAssess=shouldBeCorrect
checkedNum=[]   #number we checked already can't appear again, so if it's checked any more times after the 1st, it's wrong
# uncheckedNum=[1,2,3,4,5,6,7,8,9]
uncheckedNum=["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(len(toAssess)):              # "for 9 times, and i goes 0 to 8"
  for j in range(len(toAssess[i])):         #i is 0. "for 9 times, j goes 0 to 8" 
    if toAssess[i][j] in checkedNum:  #TypeError: argument of type 'int' is not iterable
      print("2 of the same number is in this row")
    elif toAssess[i][j] in uncheckedNum:      #j is 0, 'if this number is anywhere 1-9'.  [0][0] is 5, so toAssess[i][j] is 5 for now. 
      checkedNum.append(toAssess[i][j])
      # uncheckedNum.pop(toAssess[i][j]-1)   #if 5 (aka.toAssess[i][j]) is in uncheckedNum then it is at position unCheckedNum[5-1]   
#     IndexError: pop index out of range
      print(checkedNum) # printed 5, from [0][0]
      print(uncheckedNum)

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
