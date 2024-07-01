'''
File manager (CLI) Program in python

operations :
-ls :
    ls stands for list directory
    this operation fetches all files and directories from pwd 

    it has 3 modes :
    -s(default): this mode fatches visible files and directories
    -a: this mode fatches all visible and hidden directories and files
    -l: fetches all files and directories with states


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
import pwd as fileMetaDataFetcher
import grp
import time

root= os.getcwd()
pwd= '/'

# permissions ={
#     'access': {
#         '0': '---',
#         '1': '--x',
#         '2': '-w-',
#         '3': '-wx',
#         '4': 'r--',
#         '5': 'r-x',
#         '6': 'rw-',
#         '7': 'rwx',
#     },
#     'roles':{
#         '0': 'owner',
#         '1': 'group',
#         '2': 'other',
        
#     }
# }

color_codes = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
    }
reset_code = '\033[0m'

def decode_octal_permission(octal , path):
    result= "d" if os.path.isdir(path) else "-"

    value_letters = [ (4,'r'),(2,'w'), (1,'x') ]

    for permission in [int(n) for n in str(octal)]:
        for [value,letter] in value_letters:
            if permission >= value :
                result+= letter
                permission-=value
            else:
                result+="-"
    
    return result

def _print_colored(text,color):
    print(color_codes[color] + text + reset_code,end="\t\t")

def _decodeUnixDate(unixDate):
    date= time.localtime(unixDate)

    filterdDate= str(date.tm_mday) + '/' + str(date.tm_mon) + '/' + str(date.tm_year)

    return filterdDate

def help():
    print("Welcome to the help section here is all the details you need:")
    # all the help topic here
    
    #ls help
    print("-ls : \n \tls stands for list directory\n \tthis operation fetches all files and directories from pwd \n\n \tit has 3 modes :\n \t-s(default): this mode fatches visible files and directories\n \t-a: this mode fatches all visible and hidden directories and files\n \t-l: fetches all files and directories with states")


def ls(command):
    try:
        path=root+pwd
        dirs= os.listdir(path)

        command_options= {
            '-l': 'l', #meta daata also like permisions and size
            '-a': 'a', #all (hidden also)
            '-s': 's', # short
        }
    
        if len(command) > 1:
            listType= command_options.get(command[1])
        else:
            listType= 's'
        
        i=0
        if listType == 's' :
            for dir in dirs:
                if dir[0] == '.':
                    continue
                elif(os.path.isdir(path+dir)):
                    _print_colored(dir,'blue')
                else:
                    print(dir,end="\t\t")
                i+=1
        elif listType == 'l':
            #format : permissions owner group filesize modifiedTime filename
            for dir in dirs:
                fileStat= os.stat(path+dir)
                Permission_in_octal= oct(fileStat.st_mode)[-3:]
                
                mtimeArray=time.localtime(fileStat.st_mtime) 
                
                filteredFileStat={
                    'permissions': decode_octal_permission(Permission_in_octal , path+dir),
                    'owner':fileMetaDataFetcher.getpwuid(fileStat.st_uid).pw_name,
                    'group':grp.getgrgid(fileStat.st_gid).gr_name,
                    'size': fileStat.st_size,
                    'mtime': _decodeUnixDate(fileStat.st_mtime),
                    'fileName': dir,
                }

                for stat in filteredFileStat.values():
                    print(stat ,end="\t")
                print()
                i+=1
        elif listType == 'a':
            for dir in dirs:
                if(os.path.isdir(path+dir)):
                    _print_colored(dir,'blue')
                else:
                    print(dir,end="\t\t")
            i=len(dirs)
        else:
            raise

        print("\n Total = ",i,"\n\n")
    except:
        print(" Command not Found!!! ")




def main():
    while(True):
        print( color_codes['red'] , "( root @ Keli 2.0 ) - ["+pwd+"] $ " , reset_code ,end=" ")
        command= input()
        command= command.split(" ")

        if command[0] == 'exit':
            break
        elif command[0] == '--help' or command[0] == '-h':
            help()#not completed
        elif command[0] == 'pwd':
            print(pwd)
        elif command[0] == 'ls':
            ls(command)
        else:
            print("Command not found.")

main()