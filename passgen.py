import random
import string

print ('Hello, Welcome to Password generator')  #Welcome Message

length = int(input('\n Enter the length of password(default 8 characters)'))   #ask user for input

lower = string.ascii_lowercase #define data
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols  #Data Storage

temp = random.sample(all,length)  #generate random pass
password = "".join(temp)

all = string.ascii_letters + string.digits + string.punctuation  #eliminate data storage and generate password
password = "".join(random.sample(all,length))

print(password)
