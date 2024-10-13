GREEN='\u001b[42m'
RED='\u001b[41m'
END = '\u001b[0m'
WHITE='\u001b[47m'

for i in range(8):
    if i<2 or i>5:
        print(f'{GREEN}{" " * 31}{END}')
    elif i==2 or i==5:
        print(f'{GREEN}{" "*8}{RED}{" "*7}{GREEN}{" "*16}{END}')
    else:
        print(f'{GREEN}{" "*6}{RED}{" "*11}{GREEN}{" "*14}{END}')

for i in range(4):
    print(END)