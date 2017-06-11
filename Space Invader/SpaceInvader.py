import os
import time
import msvcrt
from ctypes import *
import sys
enemy_list = [0]
bullet_list = [0]
box_list = [0]
def prnt(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()
class enemy:
    def __init__(self, symbol, x, y, health, speedX, speedY, game):
        self.x = x
        self.y = y
        self.hp = health
        self.sX = speedX
        self.sY = speedY
        self.game = game
        #prnt(y,x,symbol)
    def move(self, dirX, dirY):
        prnt(self.y,self.x, ' ')
        self.x += dirX
        self.y += dirY
        prnt(self.y,self.x, '@')
class GameArea:
    hitBox = [[0 for a in range(237)] for b in range(62)]
    area=[[' ' for a in range(237)] for b in range(62)]
    
    def __init__(self):
        for a in range(237):
            self.area[0][a] = '#'
        for a in range(60):
            for b in range(237):
                if b == 0 or b == 236:
                    self.area[a+1][b] = '#'
        for a in range(237):
            self.area[61][a] = '#'
    def print(self):
        os.system('cls')
        for a in range(62):
            for b in range(237):
                print(self.area[a][b], end='')
def button():
    k = 0
    ret = 0
    if msvcrt.kbhit():
        k = ord(msvcrt.getch())
        if k == 27:
            ret = 1
        elif k == 119 or k == 724:
            ret = 2
        elif k == 115 or k == 804:
            ret = 3
        elif k == 97 or k == 754:
            ret = 4
        elif k == 100 or k == 774:
            ret = 5
        elif k == 32:
            ret = 6
        else:
            ret = 0
    return ret
class ship:
    shape = [' ! ',
'[|]',
'^ ^']
    x = 119
    y = 60
    lives = 3
    level = 1
    def __init__(self):
        for a in range(3):
            prnt(self.y-1+a,self.x-1,self.shape[a])
    def move(self, dir):
        c = ''
        for a in range(3):
            for b in range(3):
                if dir == -1:
                    c = self.shape[a][b]
                else:
                    c = self.shape[a][2-b]
                prnt(self.y-1+a,self.x+(2-b)*dir,c)
                #prnt(self.y+a-1,self.x-(2-b)*dir,' ')
        for a in range(3):
            prnt(self.y-1+a,self.x-dir,' ')
        self.x+=dir
class bullet:
    shape = '^'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        prnt(y,x,self.shape)
    def move(self):
        prnt(self.y,self.x,' ')
        self.y -=1
        prnt(self.y,self.x,self.shape)
def fire(x, y, level):
    type=[[1,0,0,0],[2,0,0,0],[2,1,0,0][4,0,0,0],[4,1,0,0],[4,1,1,0],[4,3,0,0],[4,3,1,0],[4,3,2,0],[4,3,2,1]]
    i=0
    for a in type[level-1]:
        i+=1
        for b in range(a):
            bullet_list.append(bullet(x-2+2*b+a%2,y-1-i))
            prnt(y-1-i,x-2+2*b+a%2,'^ ')
class box:
    shape = '$'
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        prnt(self.y,self.x,' ')
        self.y +=1
        prnt(self.y,self.x,self.shape)
def spawn(x, y, distX, distY, speedX, speedY, shape, health):
    cornerX = 119-x*(distX+1)/2
    cornerY = 27-y*(distY+1)/2
    for a in range(y):
        for b in range(x):
            prnt(cornerY+a*(distY+1),cornerX+b*(distX+1), shape)
            #enemy_list.append(enemy(shape,cornerX+b*(distX+1),cornerY+a*(distY+1),health,speedX,speedY))
def reward(x, y):
    box_list.append(box(x,y))
    prnt(y,x,'$')
f = GameArea()
f.print()
ss = ship()
#s = enemy('@', 50, 50, 1, 2, 2)
spawn(20,10,11,4,1,1,'@', 1)
event=0
while True:
    event = int(button())
    if event == 2:
        s.move(0,-1)
    elif event==3:
        s.move(0,1)
    elif event==4:
        ss.move(-1)
    elif event==5:
        ss.move(1)
    elif event==6:
        k = bullet(ss.x,ss.y-2)
    elif event == 1:
        break



