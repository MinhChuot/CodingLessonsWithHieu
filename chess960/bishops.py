position=[
['N','B','B','N','R','Q','K','R'],
['','','','','','','',''],
['','','','','','','',''],	
['','','','','','','',''],	
['','','','','','','',''],	
['','','','','','','',''],	
['','','','','','','',''],
['n','b','b','n','r','q','k','r'],
]
# horiGaps is even + vertGaps is odd = opposite
# horiGaps is odd + vertGaps is odd = same color
# horiGaps is even + vertGaps is even = same color
# horiGaps is odd + vertGaps is even  = opposite

# rowsBetweenBish=[] #difference of i's
# colsBetweenBish=[] #difference of j's

# Bishops:
	# scan board
		# find bishops, i.e. if B or b, print [i][j]
	# the bishops' positions are i+1
	# assign the position numbers (i.e. both (i+1)'s) into variables a and b
	# if a>b, then gapBetweenBishops = a-b
	# elif b>a, then gapBetweenBishops = b-a
	# if gapBetweenBishops = 1 or =3 or =5 or =7, then the Bishop Rule has been broken
	# elif =0 or =2 or =4 or =6, then proceed as normal
	
def checkBishops(board):
	numWhiteBish=[]
	numBlackBish=[]
	for rank in range(8):
		for file in range(8):
			if board[rank][file]=='B': 
				numWhiteBish.append((rank,file))
			if board[rank][file]=='b':
				numBlackBish.append((rank,file))
	if len(numWhiteBish)+len(numBlackBish)!=4:
		print("There needs to be 2 white and 2 black bishops")
		exit()
	bishop1=numWhiteBish[0]
	bishop2=numWhiteBish[1]
	bishop1Color=getColor(bishop1[0],bishop1[1])
	bishop2Color=getColor(bishop2[0],bishop2[1])

	bishop3=numBlackBish[0]
	bishop4=numBlackBish[1]
	bishop3Color=getColor(bishop3[0],bishop3[1])
	bishop4Color=getColor(bishop4[0],bishop4[1])

	if bishop1Color==bishop2Color:
		exit(f"Error: Both white bishops are on a {bishop1Color} square.")
	if bishop3Color==bishop4Color:
		exit(f"Error: Both black bishops are on a {bishop3Color} square.")

	print("Bishops are ok")


def getColor(rank,file):
	rankIsOdd=((rank+1)%2==1)
	fileIsOdd=((file+1)%2==1)
	if rankIsOdd and fileIsOdd:
		return "light"
	if not rankIsOdd and not fileIsOdd: #if both even
		return "light"
	#else
	return "dark"

checkBishops(position)