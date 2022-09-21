answer='agamemnon'
answerAsList = ['a','g','a','m','e','m','n','o','n']

showAnswer=[]
for i in range(len(answerAsList)):
	showAnswer.append("_")

DoNotRepeat=[]

j=0
gameOver=5 	#should be 10

for w in range(24):
	guess=input('Guess a letter or the word: ') ##'Guess a letter or submit "exit" if you want to close the game: '
	if guess=="exit": 	#exit button
		break
	if guess==answer:
		print("You win!")
		break
	if guess in answerAsList: 		#if right guess made
		print(guess, 'is correct') 	## you see this
		for i in range(len(answerAsList)):	#'cos we need to CHECK ALL SLOTS in the list
			if guess==answerAsList[i]: 		#finding right place for right guess in 1 list
				showAnswer[i]=guess 		#putting the guess to the same slot in a different, same-length list
		print(' '.join(showAnswer)) 	##joins list elements with space 
										##and replace empty elements with underscore
#TODO: september 17. how to stop guessing letters and guess the whole word?
		if showAnswer==answerAsList:	#if all right guesses are made
										#aka. showAnswer has been filled up correctly
			print("Congratulations. You won!")
			break
	else: #if wrong guess made
		if guess in DoNotRepeat:	#if it's wrong and also same as a previous guess 
									#(i.e. is in DoNotRepeat)
			print("You've already made this guess. Make a different guess.")	##
		else:	#if it's wrong and not the same as a previous guess
			DoNotRepeat.append(guess) 	
		j+=1
		if j==gameOver:
			print(f"Game over. You've made {gameOver} wrong guesses")	##called an f-string.
			break
		else:
			print(f"Guess again. Number of guesses left: {gameOver-j}")	##