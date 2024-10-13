GREEN='\u001b[42m'
RED='\u001b[41m'
END = '\u001b[0m'
file = open('sequence.txt')
a=[float(i) for i in file.readlines()]
sum1=sum2=0
for i in range(125):
    sum1+=abs(a[i])
length=len(a)
for i in range(length-125,length):
    sum2+=abs(a[i])
sum=sum1+sum2
per1,per2= sum1/sum,sum2/sum
print(f'Первые 125 чисел:   {RED}{" "*round(100*per1)}{END}')
print(f'Последние 125 чисел:{GREEN}{" "*round(100*per2)}{END}')