import os
import time
# import pandas as pd
# import matplotlib as mt

# print(os.listdir())
# print(os.getcwd())
# print(time.localtime(1719468562))


# print(os.path.isdir(os.getcwd()+"test.py"))
# mt.rcParams['text.color'] = 'Blue'
# print("hello")
# mt.Color='blue'
# print('hello')
# with os.scandir() as atr:
#     for a in atr:
#         mask=oct(a.stat().st_mode)
#         print(mask )


def octal_to_string(octal):
    result=""
    value_letters = [ {4,'r'},{2, 'w'}, {1, 'x'} ]

    for permission in [int(n) for n in str(octal)]:
        for value,letter in value_letters:
            if(permission >= value):
                result+= letter
                permission-=value
            else:
                result+="-"
    
    return result



print ( octal_to_string(775) )
# print( a for  as a)