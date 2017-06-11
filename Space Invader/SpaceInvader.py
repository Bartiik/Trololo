import os
import time
import msvcrt
from ctypes import *
import sys
def prnt(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

class ship:
    def __init__(self,id, game, symbol, centerx, centery, health, speedX, speedY, fire):
        self.id = id
        self.game = game
        self.shape = symbol
        self.x = centerx
        self.y = centery
        self.hp = health
        self.sX = speedX
        self.sY = speedY
        self.fire = fire
    def spawn(self):
        self.game.area[self.y][self.x] = self.shape
        self.game.hitBox[self.y][self.x] = self.id
    def move(self, dirX, dirY):
        prnt(self.y,self.x, ' ')
        self.game.hitBox[self.y][self.x] = 0
        self.x += self.sX*dirX
        self.y += self.sY*dirY
        prnt(self.y,self.x, '@')
        self.game.hitBox[self.y][self.x] = self.id
##        prnt(self.y+self.sX*dirY,self.x+self.sX*dirX, self.shape)
##        self.game.hitBox[self.y+self.sX*dirY][self.x+self.sX*dirX] = self.id
class GameArea:
    area=[[' ' for a in range(237)] for b in range(62)]
    hitBox = [[0 for a in range(237)] for b in range(62)]
    
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
    
f = GameArea()
s = ship(1, f, '@', 50, 50, 1, 2, 2, 0)
s.spawn()
f.print()
s.move(1,1)
event=0
while True:
    event = int(button())
    if event == 2:
        s.move(0,-1)
    elif event==3:
        s.move(0,1)
    elif event==4:
        s.move(-1,0)
    elif event==5:
        s.move(1,0)
    elif event == 1:
        break