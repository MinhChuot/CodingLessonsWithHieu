# position=[
# ['n','b','b','n','r','q','k','r''] 
# ['p','p','p','p','p','p','p','p']
# ['','','','','','','','']	#8
# ['','','','','','','','']	#8
# ['','','','','','','','']	#8
# ['','','','','','','','']	#8
# ['P','P','P','P','P','P','P','P']
# ['N','B','B','N','R','Q','K','R']
# ]


# print("While following the rules, please input a back rank configuration when prompted.")
# print("The rules are: 1)there can be only 2 knights, 2 bishops, 2 rooks, 1 queen and 1 King and 8 pawns,")
	# 1st rule should include "...and 8 pawns," at the end only when asking for full board configuration, which is the advanced step
# print("and 2)The bishops must be on opposite-colored-squares")

validPieces=["n","N","b","B","r","R","q","Q","k","K","p","P"]
takeBackRank=input("Write down your back rank configuration, e.g.nbbnrqkr or NBBNRQKR, but please do not intermix lower and upper case. Or submit 'exit' to end the program: ")
if takeBackRank=="exit":
	exit()
checkValidity=list(takeBackRank)
print(checkValidity)
# countN=[]
# countB=[]
# countR=[]
# countQ=[]
# countK=[]
for i in range(len(checkValidity)):
	if checkValidity[i] not in validPieces:
		print("Invalid initial letter of chess piece entered. Terminating program")
		exit()
	# if checkValidity[i]=="n" or checkValidity=="N":
	# 	countN.append(checkValidity[i])
	# 	# if len(countN)!=2:
	# 	# 	print("Invalid number of Knights. Exiting program") #how to go back to a scriptline? 
	# 	# 	exit()
	# elif checkValidity[i]=="b" or checkValidity=="B":
	# 	countB.append(checkValidity[i])
	# elif checkValidity[i]=="r" or checkValidity=="R":
	# 	countR.append(checkValidity[i])
	# elif checkValidity[i]=="q" or checkValidity=="Q":
	# 	countQ.append(checkValidity[i])
	# elif checkValidity[i]=="k" or checkValidity=="K":
	# 	countK.append(checkValidity[i])
def checkPieceCount(piecePlace,pieceList,positionNumber):
	count=[]
	if pieceList[positionNumber]==piecePlace: #if the first/2nd/3rd/etc piece is ... (e.g. "n")
		count.append(piecePlace)
		if len(countN)!=2:
			print("Invalid number of Knights. Exiting program") #how to go back to a scriptline? 
			exit()
	# for x in range(y)
for j in range(len(checkValidity)):
	x=checkPieceCount(checkValidity[j], checkValidity,j)
# board=[]
	# 	board.append(checkValidity)

# count the knights, bishops, rooks, queen/s and king/s
	# and for advanced step, count the pawns
# find the first bishop
# find the second bishop
# the bishops' positions are i+1
# assign the position numbers (i.e. both (i+1)'s) into variables a and b
# if a>b, then gapBetweenBishops = a-b
# elif b>a, then gapBetweenBishops = b-a
# if gapBetweenBishops = 1 or =3 or =5 or =7, then the Bishop Rule has been broken
# elif =0 or =2 or =4 or =6, then proceed as normal