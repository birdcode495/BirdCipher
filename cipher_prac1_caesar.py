
# Caesar Cipher Notebook 1

#from CipherTexts import *
from secret_messages import *

MAX_KEY_SIZE = 26

#cipherText_nbk1_jg = cipherText_nbk1


# def getMode():

# 	while True:

# 		print('Do you wish to decrypt or encrypt a message?')
# 		mode = input().lower()
		
# 		if mode in 'encrypt e decrypt d'.split():
			
# 			return mode

# 		else:
# 			print('Enter either "encrypt" or "e" or "decrypt" or "d" ')



def getMessage():

	# global cipherText_nbk1

	# message = cipherText_nbk1[]

	# return message

	#message = cipherText_nbk1_jg[0]

	message = secret_messages[2]

	return message

def getKey():

	key = 0
	
	

	print()
	print(" ----------------------------------------- Secret key to decrypt this message -------------------------------------------")
	print()

	key = input('         Enter your key between 1 and 26: ')

	try:
		key = int(key)

		if (key >= 1 and key <= MAX_KEY_SIZE):
			print("         Secret key saved.")

		else:
			print("         The key you have entered is not between 1 and 26. You failed.")

	except ValueError:
		print("         You entered an invalid key. You failed.")

	print()
	print(" ------------------------------------------------------------------------------------------------------------------------")

	return key

		



def getTranslatedMessage(message, key):

	#if mode[0] == 'd':

	key = -key

	translated = ''

	for symbol in message: 
		if symbol.isalpha():

			num = ord(symbol)
			num += key

			if symbol.isupper():

				if num > ord('Z'):
					num -= 26

				elif num < ord('A'):
					num += 26

			elif symbol.islower():

				if num > ord('z'):
					num -= 26

				elif num < ord('a'):
					num += 26

			translated += chr(num)

		else:
			translated += symbol

	return translated


#mode = getMode()
#message = getMessage()
#key = getKey()


# print('Your translated text is: ')
# print()
# print(getTranslatedMessage(mode, message, key))







