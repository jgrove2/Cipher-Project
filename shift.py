def encrypt(message, shift):
	shift = int(shift)
	result = ""
	for i in range(len(message)):
		char = message[i]

		if(char.isupper()):
			result += chr((ord(char)+ shift-65) % 26 + 65)
		elif(char.islower()):
			result += chr((ord(char) + shift-97) % 26 + 97)
		else:
			result += char
	return result

def decrypt(message, shift):
	shift = int(shift)
	result = ""
	for i in range(len(message)):
		char = message[i]

		if(char.isupper()):
			result += chr((ord(char) - shift-65) % 26 + 65)
		elif(char.islower()):
			result += chr((ord(char) - shift-97) % 26 + 97)
		else:
			result += char
	return result