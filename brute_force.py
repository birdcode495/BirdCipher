
print()
print()
print(" *******************************************************************************************************************************")
print()
print()
print("                                                             BIRDCIPHER                                                         ")
print()
print()
print("                                   Algorithm development to implement the Cesar Cipher in Python                                ")
print()
print()
print("                                                     Decrypting with brute force                                                ")
print()
print()
print("                                                           CRYPTANALYSIS                                                        ")
print()
print()
print(" *******************************************************************************************************************************")
print()
print()


print("                                                Cipher text: Gjudjh-ipxats wjbbxcvqxgs                                          ")
print()
print()
print(" *******************************************************************************************************************************")



MAX_KEY_SIZE = 26



def getMode():

	while True:

		print()
		print('Do you wish to decrypt or encrypt or brute force a message?')
		print()
		mode = input("Answer here: ").lower()
		
		if mode in 'encrypt e decrypt d brute b'.split():
			
			return mode

		else:
			print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b"')



def getMessage():

	# global cipherText_nbk1

	# message = cipherText_nbk1[]

	# return message

	#message = cipherText_nbk1_jg[0]

	print()
	message = input("Enter message to encrypt: ")
	print()

	return message

def getKey():

	key = 0
	
	while True:

		key = int(input('Enter your key between 1 and 26: '))
		print()

		if (key >= 1 and key <= MAX_KEY_SIZE):
			return key



def getTranslatedMessage(mode, message, key):

	if mode[0] == 'd':

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


mode = getMode()
message = getMessage()

if mode[0] != 'b':

	key = getKey()


print('Your translated text is: ')
print()

if mode[0] != 'b':

	print(getTranslatedMessage(mode, message, key))

else:

	for key in range(1, MAX_KEY_SIZE + 1):

		print("Key: ", key, " text: ",  getTranslatedMessage('decrypt', message, key))










