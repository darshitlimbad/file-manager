'''
File manager (CLI) Program in python

operations :

'''

# print("---------- File Manager in python----------")

print("----------------------------------------------------------------------")
print(" |--------------    _ _    |                      ________________    ")
print(" |--------------   |   |   |                    ||----------------    ")
print(" |                  \\ /    |                    ||                    ")
print(" |                         |                    ||                    ")
print(" |                   |     |                    ||                    ")
print(" | - - - - - - -     |     |                    ||-----------------   ")
print(" |                   |     |                    ||                    ")
print(" |                   |     |                    ||                    ")
print(" |                   |     |                    ||                    ")
print(" |                   |     |                    ||-----------------   ")
print(" |                   |     |__________________  ||_________________   ")
print("----------------------------------------------------------------------")

print("---")
print("Here you can do many things with Files and Dir/forders.")
print("--help or -h for help and details of the cammands and what it does -_-.")
print("--- \n\n\n\n") 

import os
root= os.getcwd()
pwd= '/'

def help():
    print('help')
    # all the help topic here

def ls(command):
    try:
        dirs= os.listdir(root+pwd)

        listType= 's' # s= short a= all (hidden also) l= meta daata also like directory/file admin group 
        if len(command) > 1:
            if command[1] == '-a':
                listType= 'a'
            elif command[1] == '-l':
                listType== 'l'


        for dir in dirs:
            if listType == 's' and dir[0] == '.':
                continue
            print(dir)
    except:
        print(" NO directory found ")




def main():
    while(True):
        print("( root @ Keli 2.0 ) - ["+pwd+"] $ ",end=" ")
        command= input()
        command= command.split(" ")

        if command[0] == 'exit':
            break
        elif command[0] == '--help' or command[0] == '-h':
            help()
        elif command[0] == 'ls':
            ls(command)

main()