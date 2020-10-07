value = input("Enter your Text to encrypt: ")
s = int(input(("Enter the number of shift: ")))

def encrypt(value,s): 
	result = "" 

	for i in range(len(value)): 
		char = value[i] 

		if (char.isupper()): 
			result += chr((ord(char) + s-65) % 26 + 65) 

		else: 
			result += chr((ord(char) + s-97) % 26 + 97) 

	return result 

print("Text : " + value)
print("Shift : " + str(s))
print("Cipher: " + encrypt(value,s))
