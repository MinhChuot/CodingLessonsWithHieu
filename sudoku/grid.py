class Row: 
	def __init__(self, numbers): 	

#The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods 
# in a way that makes the instance to which the method belongs be passed automatically, but not received automatically.
#the first parameter of methods (in our case... self?) is the instance the method is called on. 
#Self is always pointing to Current Object.
# Self is the first argument to be passed in Constructor and Instance Method.
# Self is a convention and not a Python keyword .	
# https://www.geeksforgeeks.org/self-in-python-class/

		self.numbers=numbers
		self.notAVariable=9

# calling the class with assigning to an instance also passes whatever parameters you put in the instance 
# to __init__... right?

	def has9(self):  

		# returns 'true' if len(r1.has9) or len(r2.has9) or etc is 9 and 'false' if otherwise
		return len(self.numbers)==9 

	#add stuff and test
	# def something else
# 	def __init__(notSelf, letters, chessPiece):
# 		notSelf.letters=letters
# 		notSelf.chessPiece=chessPiece
# 		def is_it_a_vowel(otherThanSelf, vowels):

# 			# return whether a letter in designated list of letters is a vowel or not
# 			return vowels in otherThanSelf.letters
# r5=Row(["a","b","c","d","e"],["Knight", "Bishop", "Rook", "Queen", "King"])
# print("Is a vowel") if r5.otherThanSelf("a") else print("is not a vowel")
# print("Is a vowel") if r5.otherThanSelf("e") else print("is not a vowel")
# print("Is a vowel") if r5.otherThanSelf("i") else print("is not a vowel")
# print("Is a vowel") if r5.otherThanSelf("o") else print("is not a vowel")
# print("Is a vowel") if r5.otherThanSelf("u") else print("is not a vowel")
# Lines 25-37: attempt at reproducing something in https://www.tutorialspoint.com/self-in-python-class

# https://www.w3schools.com/python/gloss_python_self.asp probably showed why im wrong

r1=Row([2,6,8]) 
r2=Row([3,5,7,2,4,6,1,9,8])
r3=Row(["a","b","c","d","e"])
r4=Row(["Knight", "Bishop", "Rook", "Queen", "King"])
# r1.numbers=[11,2,3]
print(f"Instance r1:{r1.numbers}")
print(f"Instance r2:{r2.numbers}") #not calling r1.__init__
print(f"self.notAVariable just has a 9, so this prints:{r1.notAVariable}")	#the [2,6,8] was passed but not used
print(r1.has9())
print(r2.has9())