answerAsList = []
showAnswer=[]

doNotRepeat=[]

numMistakes=0 
gameOver=10

answer=input('Write down your hangman guessword: ')
answerAsList=list(answer)
for i in range(len(answerAsList)):
	showAnswer.append("_") #a list of underscores
print(f"Your hangman guessword is '{answer}'. We may begin hangman")
#TODO: handle spaces in the answer, e.g. "long live the king"
while True:
	guess=input('Guess a letter or the word, or submit "exit" if you want to close the game: ') 
	if guess=="exit":
		exit() #previously 'break'
	if guess==answer:
		print("You win!")
		break
	if guess in answerAsList: 		#if right guess made
		print(guess, 'is correct') 	
		for i in range(len(answerAsList)):	#'cos we need to CHECK ALL SLOTS in the list
			if guess==answerAsList[i]: 		#if guess is the same as inside one or more slot/s as we pass by the list
				showAnswer[i]=guess 		#put the guess in the same slot/s in a different, empty, same-length list
		print(' '.join(showAnswer)) 	##joins said list elements with space and print
		if showAnswer==answerAsList:	#if all right guesses are made, aka. showAnswer has been filled up correctly
			print("Congratulations. You won!")
			break
	else: 							#if wrong guess made
		if guess in doNotRepeat:	#if it's wrong and also same as a previous guess (i.e. is in doNotRepeat)
			print("You've already made this guess. Make a different guess.")
		else:	#if it's wrong and not the same as a previous guess
			doNotRepeat.append(guess) 	
			numMistakes+=1
			if numMistakes==gameOver:
				print(f"Game over. You've made {gameOver} wrong guesses")	
				break
			else:
				print(f"Guess again. Number of guesses left: {gameOver-numMistakes}")	