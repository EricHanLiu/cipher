import math
import time
from random import randint

print "1: Encrypt"
print "2: Decrypt"
choice = raw_input()

if (choice == "1"):
	phrase = raw_input("Enter Phrase:\n").lower().replace(" ", "{")
	phrase.replace(" ", "`")
	output = []
	
	key = input("Enter Key:") #number of random digits to add

	#converts letters to numbers starting at 1
	for character in phrase:
		number = ord(character) - 96
		if (number < 10):
			number = "0" + str(number)
		else:
			number = str(number)
		output.append(number)
	
	for i in range(0, len(output)):
		for j in range(0, key):	
			output[i] += str(randint(0,9))
	
	print
	print "Encrypting..."
	print
	time.sleep(1)
	print "".join(output)

elif (choice == "2"):
	phrase = raw_input("Enter Encrypted Phrase:\n")
	output = []
	final = []

	key = input("Enter Key: ")

	for i in range(0, len(phrase)):
		output.append(phrase[i])

	for i in range(0, len(output), key+2):
		output[i] = output[i] + output[i+1]
		output[i] = int(output[i])

	for i in range(0, len(output), key+2):
		output[i] += 96
		output[i] = chr(output[i]).replace("{", " ")
		final.append(output[i])

	print
	print "Decrypting..."
	print
	time.sleep(1)
	print "".join(final)

else:
	print "Invalid Choice"
	system.exit(0)
