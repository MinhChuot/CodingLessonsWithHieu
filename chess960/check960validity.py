# position=[
# ['N','B','B','N','R','Q','K','R'], 
# ['P','P','P','P','P','P','P','P'],
# ['','','','','','','',''],	#8
# ['','','','','','','',''],	#8
# ['','','','','','','',''],	#8
# ['','','','','','','',''],	#8
# ['p','p','p','p','p','p','p','p'],
# ['n','b','b','n','r','q','k','r'],
# ]
##############################################################################################################################################################################################################################

validPieces=["n","N","b","B","r","R"]
validRoyalties=["q","Q","k","K"]
validPawns=["p","P"]

# print("While following the rules, please input a back rank configuration when prompted.")
# print("The rules are: 1)there can be only 2 knights, 2 bishops, 2 rooks, 1 queen and 1 King [and 8 pawns] on each side,")
	# 1st rule should include "...and 8 pawns," at the end ONLY WHEN asking for full board configuration, which is the advanced step
# print("and 2)The bishops must be on opposite-colored-squares")

takeBackRank=input("Write down your back rank configuration, e.g.nbbnrqkr or NBBNRQKR (please do not intermix lower and upper case), or submit 'exit' to end the program: ")
if takeBackRank=="exit":
	exit()
checkBackRank=list(takeBackRank)
print(checkBackRank)
# countN=[]
# countB=[]
# countR=[]
# countQ=[]
# countK=[]
for i in range(len(checkBackRank)):
	if checkBackRank[i] not in validPieces and checkBackRank[i] not in validRoyalties and checkBackRank[i] not in validPawns:
		exit("Invalid initial/s of chesspiece/s entered. Terminating program")
	# if checkBackRank[i]=="n" or checkBackRank=="N":
	# 	countN.append(checkBackRank[i])
	# 	# if len(countN)!=2:  
	# 	# 	print("There needs to be 2 knights. Exiting program") #how to go back to a scriptline? 
	# 	# 	exit()
	# elif checkBackRank[i]=="b" or checkBackRank=="B":
	# 	countB.append(checkBackRank[i])
	# elif checkBackRank[i]=="r" or checkBackRank=="R":
	# 	countR.append(checkBackRank[i])
	# elif checkBackRank[i]=="q" or checkBackRank=="Q":
	# 	countQ.append(checkBackRank[i])
	# elif checkBackRank[i]=="k" or checkBackRank=="K":
	# 	countK.append(checkBackRank[i])
def checkNumPiece(pieceInitial,pieceList,positionNumber):
	count=[]
	if pieceList[positionNumber]==pieceInitial: #if the first/2nd/3rd/etc piece is ... (e.g. "n")
		count.append(pieceInitial)
	if pieceInitial in validPieces:
		if len(count)!=2:
			exit("There needs to be 2 Bishops, 2 Knights and 2 Rooks. Exiting program")
	elif pieceInitial in validRoyalties:
		if len(count)!=1:
			print("Invalid number of Queen/King. Exiting program") #how to go back to a scriptline? 
			exit()	

for j in range(len(checkBackRank)):
	checkNumPiece(checkBackRank[j], checkBackRank,j)


	# for x in range(y)
	# x=checkNumPiece(checkBackRank[j], checkBackRank,j)


# count the knights, bishops, rooks, queen/s and king/s
	# and for advanced step, count the pawns

# check the Bishops