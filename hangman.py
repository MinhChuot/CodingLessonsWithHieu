# k=0
answerAsList = []
showAnswer=[]
while True:
	answer=(input('Write down your hangman guessword: ')) #'Write down a number from 0 to 9. '
	print(answer)
	# k+=1
	answerAsList.append(','.join(answer))
	print(answerAsList)
	for i in range(len(answerAsList)):
		showAnswer.append("_")
	print(showAnswer)
	# if you want to end the process of making hangman answer:
# 		StopCreating=int(input('Type "-1" to submit your Hangman answer. '))
# 		if StopCreating==-1:
# 			break
# 	# else:
# 		# go to line 19
	print(f"Your hangman guessword is {' '.join(answerAsList)}. We may begin hangman")
	break

# TODO: ^
# 		|  september 18
################################################

# answerAsList = [7 , 3 ,5 , 5 , 6 ,0 , 8 ]
# answer='agamemnon'
# answerAsList = ['a','g','a','m','e','m','n','o','n']

# showAnswer=[]
# for i in range(len(answerAsList)):
# 	showAnswer.append("_")

DoNotRepeat=[]

j=0
gameOver=5 	#should be 10

for w in range(22): #to Hieu: how do i do While True: correctly?
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
			print("You've already made this guess. Make a different guess.")
			break
		else:	#if it's wrong and not the same as a previous guess
			DoNotRepeat.append(guess) 	
			j+=1
			if j==gameOver:
				print(f"Game over. You've made {gameOver} wrong guesses")	##called an f-string.
				break
			else:
				print(f"Guess again. Number of guesses left: {gameOver-j}")	##