#!/usr/bin/python

import sys
import string

def main():
	if str(sys.argv[1]) == '-e':
		key = int(sys.argv[2])
		translated = ''
		message = str(sys.argv[3])
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


		print('Cipher Text:')
		print(translated)	

	
	

if __name__ == "__main__":
    main()

