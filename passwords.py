#! python3
# passwords.py - A very simple program to store your passwords.
import sys, random, shelve, pyperclip, os

# Variable 'characters' stores all possible characters to be used in a password and is randomized for the password
characters = '`1234567890-=~!@#$%^&*()_+qwertyuiop[]\\asdfghjkl;\'zxcvbnm,\"./QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?'
characters = list(characters)
random.shuffle(characters)
characters = ''.join(characters)


# Stores commandline argument in variable 'command'
command = sys.argv
del command[0]
if command == []:
    sys.exit()

file = shelve.open('PasswordData')
# Adds password info to file
if command[0] == 'a' or command[0] == 'add':
    if len(command) == 3:
        file[command[1]] = command[2]
    else:
        file[command[1]] = characters[:16]
        pyperclip.copy(characters[:16])
# Copies password for website entered
elif command[0] == 's' or command[0] == 'search':
    pyperclip.copy(file[command[1]])
# Deletes a password
elif command[0] == 'del' or command[0] == 'delete':
    file.pop(command[1])
file.close()
