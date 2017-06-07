import random

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letters = vowels+consonants

numberOfString = int(input("Enter the number of Words you want to generate: "))
lengthOfString = int(input("Enter the length of the word you want to generate: "))
constraintBoolean = input("Do you want to put any constraint on the letters? 'y' for Yes | 'n' for No: ")

constraintInputArray = ''
if (constraintBoolean == 'y'):
	for i in range(lengthOfString):
		constraintInput = input("What letter do you want? Enter '1' for vowels, '2' for consonants, '3' for any letter, '<letter>' for that particular letter: ")
		constraintInputArray += constraintInput

def generateWord(len,constraint):
	word = '';
	if(constraint == ''):
		for i in range(len):
			word += random.choice(letters)
	else:
		for i in range(len):
			if (constraint[i] == '1'):
				word += random.choice(vowels)
			elif (constraint[i] == '2'):
				word += random.choice(consonants)
			elif (constraint[i] == '3'):
				word += random.choice(letters)
			else:
				word += constraint[i]

	return word

print("\nGenerated Words: \n")
for i in range(numberOfString):
	print("\t" + str(i+1) + "." + " " + generateWord(lengthOfString, constraintInputArray))