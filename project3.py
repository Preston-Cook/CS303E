# File: Project3.py
# Student: Preston Cook
# UT EID: plc886
# Course Name: CS303E
# 
# Date: 12/17/2022
# Description of Program: Substitution Cipher

import random as r
import string

# Global Letters Variable
LETTERS = string.ascii_lowercase
VALID_COMMANDS = ['getkey', 'changekey', 'encryptfile', 'decryptfile', 'quit']


def main():
    cipher = SubstitutionCipher()
    while True:
        user_input = input('Enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ').lower()
        
        while user_input not in VALID_COMMANDS:
            print('Command not recognized. Try again!\n')
            user_input = input('Enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ').lower()
        
        if user_input == VALID_COMMANDS[0]:
            print(f'  Current Cipher Key: {cipher.getKey()}')
        
        elif user_input == VALID_COMMANDS[1]:
            user_key_change = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()

            while user_key_change not in ['quit', 'random'] and not isValidKey(user_key_change):
                print('Illegal key entered. Try again!')
                user_key_change = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()
            
            if isValidKey(user_key_change):
                cipher.setKey(user_key_change)
                print(f'    New cipher key: {user_key_change}')
            
            elif user_key_change == 'random':
                new_key = makeRandomKey()
                cipher.setKey(new_key)
                print(f'    New cipher key: {new_key}')
        
        elif user_input == VALID_COMMANDS[2]:
            filename = input('  Enter a file name: ')
            
            try:
                cipher.encryptFile(filename)
                print(f"The encrypted output filename is {filename[:-4] + '-Enc.txt'}")

            except FileNotFoundError:
                print('File does not exist')

        elif user_input == VALID_COMMANDS[3]:
            filename = input('  Enter a file name: ')

            try:
                cipher.decryptFile(filename)
                print(f"The encrypted output filename is {filename[:-4] + '-Dec.txt'}")
                
            except FileNotFoundError:
                print('File does not exist')

        elif user_input == VALID_COMMANDS[4]:
            print('Thanks for visiting!')
            return 0
        
        print()

# Auxillary functions
def makeRandomKey():
    lst = list(LETTERS)    
    r.shuffle(lst)   
    return ''.join(lst)    

def isValidKey(key):
    return all(char in key for char in LETTERS)

def makeConversionDictionary(key1, key2):
    key1, key2 = map(str.lower, (key1, key2 ))

    if not isValidKey(key1) or not isValidKey(key2):
        raise ValueError
    
    return {k : v for k, v in zip(key1, key2)}


class SubstitutionCipher:
    """Create an instance of the cipher with stored key, 
    which defaults to a randomly generated key."""
    def __init__(self, key=makeRandomKey()):
        self.__key = key
    
    def setKey(self, key):
        """Setter for the stored key.  Check that it's a legal"""
        if isValidKey(key):
            self.__key = key
    
    def getKey(self):
        """Getter for the stored key."""
        return self.__key
    
    def encryptFile(self, inFile):
        """Encrypt the contents of inFile using the stored key and 
        write the results into outFile.  Assume inFile exists."""
        with open(inFile, 'r') as f:
            plain_text = f.readlines()
        
        conversion_dic = makeConversionDictionary(LETTERS, self.__key)

        with open(inFile[:-4] + '-Enc.txt', 'w') as f:
            for line in plain_text:
                encrypted_line = ''
                for char in line:
                    lowered_char = char.lower()
                    if lowered_char in conversion_dic:
                        encrypted_char = conversion_dic[lowered_char]
                        if char.isupper():
                            encrypted_char = encrypted_char.upper()
                        encrypted_line += encrypted_char
                    else:
                        encrypted_line += char
                f.write(encrypted_line)


    def decryptFile(self, inFile):
        """Decrypt the contents of inFile using the stored key
        and write the results into outFile.  Assume inFile exists."""
        with open(inFile, 'r') as f:
            encrypted_text = f.readlines()
        
        conversion_dic = makeConversionDictionary(self.__key, LETTERS)
        
        with open(inFile[:-4] + '-Dec.txt', 'w') as f:
            for line in encrypted_text:
                decrypted_line = ''
                for char in line:
                    lowered_char = char.lower()
                    if lowered_char in conversion_dic:
                        decrypted_char = conversion_dic[lowered_char]
                        if char.isupper():
                            decrypted_char = decrypted_char.upper()
                        decrypted_line += decrypted_char
                    else:
                        decrypted_line += char
                f.write(decrypted_line)



if __name__ == '__main__':
    main()