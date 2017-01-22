#!/usr/bin/python

import sys
import string

def main():
	if str(sys.argv[1]) == '-d':
		print('Decrypted Cipher Text:')
		for key in range(0,25): 
			translated = ''
			message = str(sys.argv[2])
			message = message.lower()
			for symbol in message:
				if symbol.isalpha():
					num = ord(symbol)
					num += key
					if num > ord('z'):
						num -= 26
					elif num < ord('a'):
						num += 26
					translated += chr(num)
				else:
					translated += symbol


			print(translated)	
	
if __name__ == "__main__":
    main()

