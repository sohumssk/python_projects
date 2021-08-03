#Welcome to the Password Generator Python Project
#Author: Sohum Kulkarni

import random
import pyperclip

print('Are you search for a strong and secure password? You are in the right place!')
print('Welcome to Password Generator!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()0123456789'

length = input('Password length: ')
length = int(length)

password=''
for pwd in range(length):
    password += random.choice(chars)
print(password)    

question = input('Do you want this password to be copied? (Y/N)\n')

if(question=='Y'):
    pyperclip.copy(password)
    print('Copied to Clipboard!')
    print('Have a great day!')
else:
    print('Have a good day!')

