GREEN='\u001b[42m'
RED='\u001b[41m'
END = '\u001b[0m'
WHITE='\u001b[47m'
def pattern(n,m):
    for i in range(n):
        print(f'{WHITE}{" "*15}{END}{" "*6}'*m)
        print(f'{WHITE}{" "*3}{END}{" "*9}{WHITE}{" "*3}{END}{" "*6}'*m)
        print(f'{WHITE}{" "*3}{END}{" "*3}{WHITE}{" "*9}{END}{" "*6}'*m)
        print(f'{WHITE}{" "*3}{END}{" "*3}{WHITE}{" "*3}{END}{" "*12}'*m)
        print(f'{WHITE}{" "*3}{END}{" "*3}{WHITE}{" "*15}{END}'*m)
pattern(5,4)