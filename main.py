from tkinter import *
from tkinter import messagebox
import sys
import ast
from Ciphers import rsa, rc4, shift, vigenere

needKey = False

# gives errors when the key is incorrect for a specific encryption type
def noKeyError(message):
	messagebox.showerror("Key Error", message)

# Create the variables for the options dropdown menu
def createOptionVars():
	schemes = ["Shift", "Caesar", "Vigenere", "RC4", "RSA"]
	schemeVar = StringVar(window)
	schemeVar.set("Shift")
	return schemeVar, schemes

# Create the message box and label
def createMessageBox():
	Label(window, text="Enter your message text: ", font="none 12 bold").grid(row=1, column=0, sticky=W)
	messageEntry = Entry(window, width=75)
	messageEntry.grid(row=2, column=0, sticky=W)
	return messageEntry

#Run encryption with the selected encryption scheme
def encrypt():
	entered_message = messageEntry.get()
	output.delete(0.0, END)
	selected = schemeVar.get()
	if(selected == "Caesar"):
		encrypted_message = shift.encrypt(entered_message, 3)
	elif(selected == "Shift"):
		key = keyEntry.get()
		if not isinstance(key, int):
			noKeyError("You need a key that is an integer")
			return 0
		else:
			encrypted_message = shift.encrypt(entered_message, keyEntry.get())
	elif(selected == "Vigenere"):
		key = keyEntry.get()
		if not key.isalpha():
			noKeyError("You need a key that is a word")
			return 0
		else:
			encrypted_message = vigenere.encrypt(entered_message, key)
	elif(selected == "RC4"):
		key = keyEntry.get()
		if not key:
			noKeyError("You need a key that is a word/phrase")
			return 0
		else:
			encrypted_message = rc4.encrypt(entered_message, key)
	elif(selected == "RSA"):
		pubKey = rsaKeys[0].get("0.0", END)
		if not pubKey:
			noKeyError("Generate the public and private keys or enter your own")
			return 0
		else:
			pub = pubKey.split(" ")
			# print(pub[0])
			# print(pub[1])
			encrypted_message = rsa.encrypt(entered_message, pub)
	else:
		encrypted_message = entered_message
	output.insert(END, encrypted_message)
	return 1

# Run decryption on with the selected cipher
def decrypt():
	entered_message = messageEntry.get()
	output.delete(0.0, END)
	selected = schemeVar.get()
	if(selected == "Caesar"):
		decrypt_message = shift.decrypt(entered_message, 3)
	elif(selected == "Shift"):
		key = keyEntry.get()
		if not isinstance(key, int):
			noKeyError("You need a key that is an integer")
			return 0
		else:
			decrypt_message = shift.decrypt(entered_message, keyEntry.get())
	elif(selected == "Vigenere"):
		key = keyEntry.get()
		if not key.isalpha():
			noKeyError("You need a key that is a word")
			return 0
		else:
			decrypt_message = vigenere.decrypt(entered_message, keyEntry.get())
	elif(selected == "RC4"):
		key = keyEntry.get()
		if not key:
			noKeyError("You need a key that is a word/phrase")
			return 0
		else:
			decrypt_message = rc4.decrypt(entered_message, keyEntry.get())
	elif(selected == "RSA"):
		privKey = rsaKeys[1].get("0.0", END)
		pubKey = rsaKeys[0].get("0.0", END)
		if not privKey or not pubKey:
			noKeyError("You need a private key to run the decryption")
			return 0
		else:
			decrypt_message = rsa.decrypt(entered_message, privKey, pubKey.split(" "))
	else:
		decrypt_message = entered_message
	output.insert(END, decrypt_message)
	return 1

# The only thing that this is used for is to insert the rsa keys into their specific loacations
def generateKey():
	e, d, n = rsa.getKey()
	rsaKeys[0].delete(0.0, END)
	rsaKeys[1].delete(0.0, END)
	rsaKeys[0].insert(END, [e, n])
	rsaKeys[1].insert(END, d)
	
# This changes around the layout of the GUI to be for any specific cipher
def hide(choice):
	if(choice == "Caesar"):
		keyEntry.grid_remove()
		keyText.grid_remove()
		genKey.grid_remove()
		for i in rsaKeys:
			i.grid_remove()
		for i in rsaText:
			i.grid_remove()
		encText.grid()
	elif(choice == "RSA"):
		keyEntry.grid_remove()
		keyText.grid_remove()
		genKey.grid()
		for i in rsaKeys:
			i.grid()
		for i in rsaText:
			i.grid()
		encText.grid_remove()
	else:
		genKey.grid_remove()
		keyEntry.grid()
		keyText.grid()
		encText.grid()
		for i in rsaKeys:
			i.grid_remove()
		for i in rsaText:
			i.grid_remove()

if __name__ == "__main__":
# This sets up the window for the project
	window = Tk()
	window.title("Cipher Project")
	window.configure()

# The options menu allowing for seleciton of differnt ciphers to test out and use
	schemeVar, schemes = createOptionVars()
	schemeMenu=OptionMenu(window, schemeVar, *schemes, command=hide)
	schemeMenu.grid(row=0, column = 1, sticky=W)

	# The key entry used with some of the ciphers
	keyText = Label(window, text="Enter your key:", font="none 12 bold")
	keyText.grid(row=1, column=1, sticky=W)
	keyEntry = Entry(window, width=25)
	keyEntry.grid(row=2, column=1, sticky=W)

	# Enter the message to be cyphered here
	messageEntry = createMessageBox()

	# keybox and their associated windows for the rsa encryption scheme
	rsaKeys = [Text(window, width=75, height=5, wrap=WORD), Text(window, width=75, height=5, wrap=WORD)] 
	rsaText = [Label(window, text="\nPublic Key: ", font="none 12 bold"), Label(window, text="\nPrivate Keys: ", font="none 12 bold")]
	rsaKeys[0].grid(row=5, column=0, columnspan=2)
	rsaKeys[1].grid(row=5, column=2, columnspan=2)
	rsaText[0].grid(row=4, column=0, columnspan=2)
	rsaText[1].grid(row=4, column=1, columnspan=2)

	# Buttons for encryption decryption and the generation of keys
	Button(window, text="Encrypt", width=6, command=encrypt).grid(row=3, column=0, sticky=W)
	Button(window, text="Decrypt", width=6, command=decrypt).grid(row=3, column=1, sticky=W)
	genKey = Button(window, text="Gen Keys", width=6, command=generateKey)
	genKey.grid(row=3, column=2, sticky=W)

	# Recieve the encrypted text here
	encText = Label(window, text="\nEncrypted Text: ", font="none 12 bold")
	encText.grid(row=4, column=0, sticky=W)

	# Where you receive the decrypted or encrypted text
	output = Text(window, width=75, height=6, wrap=WORD)
	output.grid(row=6, column=0, columnspan=2, sticky=W)

	hide("SHIFT")
	window.mainloop()