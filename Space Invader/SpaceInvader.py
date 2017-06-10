import os
x = int(input('give me width: '))
y = int(input('give me height:'))
list=''
os.system('cls')
for a in range(x):
    list+='@'
for a in range(y):
    print(list)

