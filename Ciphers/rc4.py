import codecs

def KSA(key):
	S = []
	for i in range(256):
		S.append(i)
	j = 0
	for i in range(256):
		j = (j + S[i]+key[i % len(key)]) % 256
		S[i], S[j] = S[j], S[i]
	return S

def PRGA(S):
	i = 0
	j = 0
	while True:
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j], S[i]
		K = S[(S[i] + S[j]) % 256]
		yield K

def RC4(key):
	S = KSA(key)
	return PRGA(S)

def encrypt(plaintext, key):
	key = [ord(c) for c in key]
	keystream = RC4(key)
	cipher_text = 0x0
	for c in plaintext:
		cipher_text = cipher_text << 8
		xor = int(hex(ord(c) ^ next(keystream)), 16)
		cipher_text = cipher_text | xor
	return hex(cipher_text)

def decrypt(cipher_text, key):
	key = [ord(c) for c in key]
	keystream = RC4(key)
	offset = (int((len(cipher_text)-2)/2)-1) * 8
	r = int((len(cipher_text)-2)/2)
	cipher_text = int(cipher_text, 16)
	for i in range(r):
		xor = next(keystream) << offset
		cipher_text = cipher_text ^ xor
		offset -= 8
	binary_str = codecs.decode(hex(cipher_text)[2:], "hex")
	return str(binary_str,'utf-8')

if __name__ == '__main__':
	enc = encrypt("man", "there are a few things wrong")
	dec = decrypt(enc, "there are a few things wrong")
	#bytes_object = bytes(dec)
	#ascii_string = bytes_object.decode("ASCII")
	print(enc)
	print(dec)
	#print(ascii_string)
