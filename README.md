# Cipher-Project
 Various ciphers are shown allowing for encryption and decryption of messages.
 ## Ciphers Included
 There are currently 4 separate ciphers included in the project. There are 5 separate options, however this is because there is one option for a ceasar cipher. This cipher is just a certain implementation of the shift cipher.
 ### Shift Cipher
 This cipher just takes in a message a key and then shifts all of the letters by that key.\n
 E<sub>n</sub>(x) = (x + n) mod 26
 D<sub>n</sub>(x) = (x - n) mod 26
### Vigenere Cipher
This cipher uses a key word to encrypt the message text. Each letter in the message text is shifted by the letters of the key word.\n
Letters A-Z are equivalent to 0-25. The encryption E using the key of K is described as.\n
E<sub>k</sub>(M<sub>i</sub>) = (M<sub>i</sub> + K<sub>i mod m</sub>) mod 26 \n
D<sub>k</sub>(C<sub>i</sub>) = (C<sub>i</sub> + K<sub>i mod m</sub>) mod 26 \n
### RC4 (Rivest Cipher 4)
The breaking of this algorithm has lead to multiple vulnerabilities in WEP. \n
The implementation of this algorithm includes the use of a PRG(Pseudo-random generator) and a KSA(Key-scheduling algorithm). Each value in the plaintext is xored with the next value in the PRG creating a encrypted text. The opposite allows for the decoding of the algorithm.
### RSA (Rivest-Shamir-Adleman)
This is a public-key cryptosystem. The implementation of this algorithm is fairly straight forward.\n
1. p and q are generated as two distinct prime numbers to be kept secret
2. n is computed by performing p*q. n is part of the public key.
3. \lambda(n) = lcm(p-1, q-1)
4. Choose and integer 1 < e < \lambda(n) where gcd(e, \lambda(n)) = 1
5. Determin d that is the multiplicative inverse of e mod(\lambda(n))
Both n and e are distributed as the public key where d is the private key.\n
Encryption:\n
m<sup>e</sup> = c(mod n)\n
Decryption:\n
c<sup>d</sup> = (m<sup>e</sup>)<sup>d</sup> = m (mod n)