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

# scanRanks=[]

# print("While following the rules, please input a back rank configuration when prompted.")
# print("The rules are: 1)there can be only 2 knights, 2 bishops, 2 rooks, 1 queen and 1 King and 8 pawns,")
	# 1st rule should include "...and 8 pawns," at the end only when asking for full board configuration, which is the advanced step
# print("and 2)The bishops must be on opposite-colored-squares")

takeBackRank=input("Write down your back rank configuration, e.g.nbbnrqkr: ")
checkValidity=list(takeBackRank)
print(checkValidity)
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