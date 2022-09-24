# a=5
# print(a)
# b=2
# print(a==b)
# c=7
# if a==5 or b==2 or c==9:
# 	print('hello world')
# else:
# 	print('check your math')
# for num in [1,2,3,4,5]:
# 	print(num+5)
# x=input()
# print('your number is',1+int(x))
##################################################################################################################################
# answer='agamemnon'
# answerAsList = ['a' , 'g' ,'a' , 'm' , 'e' ,'m' , 'n' , 'o', 'n']
##########################
# k=0
# while True:
# 	answer=int(input('Write down a number from 0 to 9. '))
# 	print(answer)
# 	k+=1
# 	# answerAsList.append(answer)
# 	# showAnswer.append("")
# 	# if you want to end the process of making hangman answer:
# 		StopCreating=int(input('Type "-1" to submit your Hangman answer. '))
# 		if StopCreating==-1:
# 			break
# 	# else:
# 		# go to line 19
############################
answerAsList = [7 , 3 ,5 , 5 , 6 ,0 , 8 ]
#take input, if input is part of answer, display input in correct place, next turn
showAnswer=[]
# for i in range(len(answerAsList)):
# 	showAnswer.append("")
j=0
# while True: #??? why did it rmb. Probably helps to WATCH SoME VIDEOS ON WHILE LOOPS
# for w in range(2):
# for w in range(3):
for w in range(11):
	guess=int(input('Call out a number from 0 to 9. '))
	# if guess==-1:
	# 	break
	print(guess)
	if guess in answerAsList: #right guess made
		print(guess, 'is correct')
		if w>=1: #if it's the 2nd Iteration onwards, don't append. Only modify the list
			for i in range(len(answerAsList)):
				if guess==answerAsList[i]:
					print('w is', w)
					print('i is', i) #why wrong guess then right guess produce error? September 10: START HERE. Is it to do with line 32?
					print('showAnswer is', showAnswer)
					showAnswer[i]=guess 
		else: 	#if it's the 1st iteration of w
				# w is 0, only do the appending in this First Iteration
			for i in range(len(answerAsList)):
				if guess==answerAsList[i]: #still in first guess
					showAnswer.append(guess)
				else:
					showAnswer.append("")
				# showAnswer.append(i)
		print(showAnswer) #cool tech
	else: #wrong guess made
		if w<1:
			for i in range(len(answerAsList)):
				showAnswer.append("")
			j+=1
			print("Guess again. Number of guesses left:", 10-j )
			if j==10:
				print("Game over. You've made 10 wrong guesses")
				break
			else:
				# go back to line 40
# lines 63 to 65 was missing.. 
# does same thing as 55 to 57 for when w is 0
		else:
			j+=1 	#the only piece of new logic is j+=1 which is interesting. try to get that working with the while loop, 
				#instead of by copying pasting code
			print("Guess again. Number of guesses left:", 10-j )
			print('showAnswer is', showAnswer)
			print('w is', w)
			if j==10:
				print("Game over. You've made 10 wrong guesses")
				break
			else:
				# go back to line 40
		###################################################################################################################
	# 	guess=int(input('Call out a number from 0 to 9. '))
	# 	# if guess==-1:
	# 	# 	break
	# 	print(guess) 
	# 	if guess in answerAsList:
	# 		print(guess, 'is correct')
	# 		for i in range(len(answerAsList)):
	# 			if guess==answerAsList[i]: #still in first guess
	# 				showAnswer.append(guess)
	# 			else:
	# 				showAnswer.append("")
	# 			# showAnswer.append(i)
	# 			print(showAnswer) 
	# # if guess == 'a' or 'g' or 'm' or 'e' or 'n' or 'o':
	# # if i==0 and guess==7 or i==3 or i==5 or i==6 or i==0 or i==8:
	# 	else:
	# 		for i in range(len(answerAsList)):
	# 			showAnswer.append("")
	# 			print(showAnswer)
	# 		j=+1
	# 		print("Guess again. Number of guesses left:", 10-j )
###################################################################################################################
	# 		guess=int(input('Call out a number from 0 to 9. '))
	# 		# if guess==-1:
	# 		# 	break
	# 		print(guess) 
	# 		if guess in answerAsList:
	# 			print(guess, 'is correct')
	# 			for i in range(len(answerAsList)):
	# 				if guess==answerAsList[i]: #still in first guess
	# 					showAnswer.append(guess)
	# 				else:
	# 					showAnswer.append("")
	# 				# showAnswer.append(i)
	# 				print(showAnswer) 
	# # if guess == 'a' or 'g' or 'm' or 'e' or 'n' or 'o':
	# # if i==0 and guess==7 or i==3 or i==5 or i==6 or i==0 or i==8:
	# 		else:
	# 			for i in range(len(answerAsList)):
	# 				showAnswer.append("")
	# 				print(showAnswer)
	# 			j=+1
	# 			print("Guess again. Number of guesses left:", 10-j )