#random password generator, password will be 2 upper case letters, 2 lower case, 2 numbers and 2 special characters

#import libraries

import random

#shuffle function

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return''.join(tempList)

#assign variables  using ASCII code

uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))

lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))

digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))

specialCharacter1 = chr(random.randint(33,36))
specialCharacter2 = chr(random.randint(33,36))

#Assign values for password
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 +digit2 + specialCharacter1 + specialCharacter2

#randomize order of password
password = shuffle(password)

#print password to console
print(password)
