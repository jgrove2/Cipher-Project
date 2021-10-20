def encrypt(message, key):
	ret = ""
	offset = 0
	message = message.upper()
	key = key.upper()
	for i in range(len(message)):
		if message[i].isalpha():
			k = ord(key[(i-offset) % len(key)]) - 65
			m = ord(message[i]) - 65
			ret += chr((m + k) % 26 + 65)
		else:
			ret += message[i]
			offset += 1
	return ret

def decrypt(message, key):
	ret = ""
	offset = 0
	message = message.upper()
	key = key.upper()
	for i in range(len(message)):
		if message[i].isalpha():
			k = ord(key[(i-offset) % len(key)]) - 65
			m = ord(message[i]) - 65
			ret += chr((m - k) % 26 + 65)
		else:
			ret += message[i]
			offset += 1
	return ret
	
if __name__ == "__main__":
	key = 'aaa'
	m = 'aaa'
	print(encrypt(m, key))
	print(ord('A'))
	print(ord('A'))
	print((ord('A')-65+ord('A')-65) % 26 + 65)