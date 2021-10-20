from math import lcm, gcd
from random import randint
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
from  Crypto.Random import get_random_bytes
# This is a public key encryption scheme
# RSA
# This can be changed to make the bit lenght of the p and q values longer
key_length = 128

def getKey():
	q = getPrime(key_length, randfunc=get_random_bytes)
	p = getPrime(key_length, randfunc=get_random_bytes)
	phi = lcm(p-1, q-1)
	n = p*q
	d = None
	while d is None:
		try:
			e = randint(2, phi)
			while gcd(n, e) != 1:
				e = randint(n, e)
			d = pow(e, -1, phi)
		except:
			continue
	return hex(e), hex(d), hex(n)

def decrypt(c, d, pubKey):
	return long_to_bytes(pow(int(c, 16), int(d, 16), int(pubKey[1], 16)))

def encrypt(m, pubKey):
	m = bytes_to_long(m.encode("utf-8"))
	return hex(pow(m, int(pubKey[0], 16), int(pubKey[1], 16)))


if __name__ == "__main__":
	
	e, d, n = getKey()

	print("n:{}, e:{}, d:{}".format(n, e, d))

	message = "hello world"
	c = encrypt(message, [e, n])
	
	res = decrypt(c, d, [e, n])

	print(c)
	print(res)