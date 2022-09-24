answerAsList = []
showAnswer=[]

DoNotRepeat=[]

j=0
gameOver=10

while True:
	answer=(input('Write down your hangman guessword: '))
	for letter in answer:
		answerAsList.append(letter)
	for i in range(len(answerAsList)):
		showAnswer.append("_")
	print(f"Your hangman guessword is {''.join(answerAsList)}. We may begin hangman")
	break

for w in range(25):
	guess=input('Guess a letter or the word, or submit "exit" if you want to close the game:  ') 
	if guess=="exit":
		break
	if guess==answer:
		print("You win!")
		break
	if guess in answerAsList: 		#if right guess made
		print(guess, 'is correct') 	
		for i in range(len(answerAsList)):	#'cos we need to CHECK ALL SLOTS in the list
			if guess==answerAsList[i]: 		#finding right place for right guess in 1 list
				showAnswer[i]=guess 		#putting the guess to the same slot in a different, same-length list
		print(' '.join(showAnswer)) 	##joins said list elements with space and replace empty elements with underscore, and print
		if showAnswer==answerAsList:	#if all right guesses are made, aka. showAnswer has been filled up correctly
			print("Congratulations. You won!")
			break
	else: #if wrong guess made
		if guess in DoNotRepeat:	#if it's wrong and also same as a previous guess (i.e. is in DoNotRepeat)
			print("You've already made this guess. Make a different guess.")
		else:	#if it's wrong and not the same as a previous guess
			DoNotRepeat.append(guess) 	
			j+=1
			if j==gameOver:
				print(f"Game over. You've made {gameOver} wrong guesses")	
				break
			else:
				print(f"Guess again. Number of guesses left: {gameOver-j}")	