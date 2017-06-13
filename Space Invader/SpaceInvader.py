import os
import time
import msvcrt
from ctypes import *
from random import randint
from threading import Thread
import sys
enemy_list = []
bullet_list = []
box_list = []
bullets = 0
enemies = 0
boxes = 0
clock = 0

#method which prints given text on given coordinates in console
def prnt(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()
     
def Timer():
    global clock
    while True:
        if clock == 100:
            clock = 0
        else:
            clock+=1
        time.sleep(0.1)
    
class enemy:
    def __init__(self, game, symbol, x, y, speedX):
        self.x = x
        self.y = y
        self.shape = symbol
        self.sX = speedX
        self.game = game
    def move(self, dirX, dirY):
        global enemy_list
        prnt(self.y,self.x, ' ')
        self.game.hitBox[self.y][self.x][0] = 0
        self.game.hitBox[self.y][self.x][1] = 0
        self.x += dirX
        self.y += dirY
        prnt(self.y,self.x, self.shape)
        self.game.hitBox[self.y][self.x][0] = 2
        self.game.hitBox[self.y][self.x][1] = enemy_list.index(self)
    def remove(self):
        global enemy_list
        global enemies
        self.game.hitBox[self.y][self.x][0] = 0
        self.game.hitBox[self.y][self.x][1] = 0
        enemies-=1
        prnt(self.y,self.x, ' ')
        enemy_list.remove(self)
class GameArea:
    hitBox = [[[0 for c in range(2)] for a in range(237)] for b in range(62)]
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

class ship:
    shape = [' ! ',
             '[|]',
             '^ ^']
    x = 119
    y = 60
    level = 1
    def __init__(self, game):
        for a in range(3):
            self.game = game
            prnt(self.y-1+a,self.x-1,self.shape[a])
    def move(self, dir):
        global box_list
        c = ''
        for a in range(3):
            if dir == -1:
                if self.game.hitBox[self.y-1+a][self.x-2][0]==4:
                    box_list[self.game.hitBox[self.y-1+a][self.x-2][1]].remove()
                    if(self.level < 10): self.level+=1
        for a in range(3):
            for b in range(3):
                if dir == -1:
                    c = self.shape[a][b]
                else:
                    c = self.shape[a][2-b]
                prnt(self.y-1+a,self.x+(2-b)*dir,c)
        for a in range(3):
            prnt(self.y-1+a,self.x-dir,' ')
            self.game.hitBox[self.y-1+a][self.x-dir][0]=0
            self.game.hitBox[self.y-1+a][self.x+dir*2][0]=1
        self.x+=dir
        
class bullet:
    shape = '^'
    def __init__(self,game, x, y):
        self.x = x
        self.y = y
        self.game = game
    def move(self):
        global bullet_list
        prnt(self.y,self.x,' ')
        self.game.hitBox[self.y][self.x][0] = 0
        self.game.hitBox[self.y][self.x][1] = 0
        self.y -=1
        prnt(self.y,self.x,self.shape)
        self.game.hitBox[self.y][self.x][0] = 3
        self.game.hitBox[self.y][self.x][1] = bullet_list.index(self)
    def remove(self):
        global bullet_list
        global bullets
        self.game.hitBox[self.y][self.x][0] = 0
        self.game.hitBox[self.y][self.x][1] = 0
        bullets-=1
        prnt(self.y,self.x,' ')
        bullet_list.remove(self)
            

class box:
    shape = '$'
    def __init__(self,game, x, y):
        self.x = x
        self.y = y
        self.game = game
    def move(self):
        prnt(self.y,self.x,' ')
        self.game.hitBox[self.y][self.x][0] = 0
        self.y +=1
        prnt(self.y,self.x,self.shape)
        self.game.hitBox[self.y][self.x][0] = 4
    def remove(self):
        global box_list
        global boxes
        self.game.hitBox[self.y][self.x][0] = 0
        self.game.hitBox[self.y][self.x][1] = 0
        boxes-=1
        prnt(self.y,self.x,' ')
        box_list.remove(self)
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

def fire(game, ship):
    global bullet_list
    global bullets
    type=[[1,0,0,0],[2,0,0,0],[2,1,0,0],[4,0,0,0],[4,1,0,0],[4,1,1,0],[4,3,0,0],[4,3,1,0],[4,3,2,0],[4,3,2,1]]
    i = 0
    for a in type[ship.level-1]:
        i+=1
        for b in range(a):
            bullets+=1
            bullet_list.append(bullet(game, ship.x+i+1+2*b-4,ship.y-1-i))
            

def spawn(game, x, y, distX, distY, speedX, shape):
    global enemy_list
    global enemies
    cornerX = int(119-x*(distX+1)/2)
    cornerY = int(27-y*(distY+1)/2)
    enemies+=x*y
    #i = 1
    for a in range(y):
        for b in range(x):
            enemy_list.append(enemy(game, shape,int(cornerX+b*(distX+1)),int(cornerY+a*(distY+1)),speedX))
def reward(game, x, y):
    global box_list
    global boxes
    boxes+=1
    box_list.append(box(f,x,y))
    prnt(y,x,'$')
    game.hitBox[y][x][1] = boxes
    game.hitBox[y][x][0] = 4

    
def enemyHit(game, item, x, y, who, dir):
    global enemy_list
    global bullet_list
    global enemies
    global bullets
    if who == 2:
        bullet_list[game.hitBox[item.y][item.x+dir][1]].remove()
        item.remove()
    else:
        enemy_list[game.hitBox[item.y-1][item.x][1]].remove()
        item.remove()
    if randint(1,100)>80:
        boxNum = reward(game, x,y)
def change(game, ship, goneDown, dir):
    global enemy_list
    global box_list
    global bullet_list
    global enemies
    global bullets
    global boxes
    global clock
    refresh_rate = 1000
    dirY = 0
    speedX = enemy_list[0].sX
    speed = 10
    if clock%speed==0:
        for a in enemy_list:
            if a.x == 236:
                dir = -1
                if goneDown==0: dirY = 1
                break
            if a.x == 2:
                dir = 1
                if goneDown==0: dirY = 1
                break
        if dirY == 1:
            for a in reversed(enemy_list):
                if a.y+1 == 57:
                    return (goneDown, dir, 1)
                a.move(0,1)
            dirY=0
            goneDown=1
        else:
            if dir == 1:
                for a in reversed(enemy_list):
                    if game.hitBox[a.y][a.x+1][0] == 3:
                        enemyHit(game,a,a.x,a.y,2, 1)
                    else:
                        a.move(1,0)
            else:
                for a in enemy_list:
                    if game.hitBox[a.y][a.x-1][0] == 3:
                        enemyHit(game,a,a.x,a.y,2,-1)
                    else:
                        a.move(-1,0)
            goneDown=0
    if clock%(speed/2)==0:
        for a in box_list:
            
                
            if a.y+1 == 1 or a.y+1 == 62:
                a.remove()
            else:
                if game.hitBox[a.y+1][a.x][0] == 1:
                    if ship.level < 10: ship.level+=1
                    a.remove()
                else:
                    a.move()
    if clock%(speed/2)==0:
        clock+=1
        for a in bullet_list:
            if a.y-1 == 1:
                a.remove()
            else:
                
                if(game.hitBox[a.y-1][a.x] == 2):
                
                    enemyHit(game,a,a.x,a.y,3, enemies, 0)
                else:
                    game.hitBox[a.y-1][a.x][1] = game.hitBox[a.y][a.x][1]
                    game.hitBox[a.y][a.x][1] = 0
                    a.move()
    return (goneDown, dir, 0)
# 0 - empty 1-ship 2-enemy 3-bullet 4-box
f = GameArea()
f.print()
ss = ship(f)
spawn(f,10,10,2,2,100,'@')
event=0
i = 0
goneDown = 0
dir = 1
defeat = 0
thread1 = Thread( target=Timer )

thread1.start()

while True:
    if enemies == 0:
        prnt(31,115,'VICTORY')
        break
    elif defeat == 1:
        prnt(31,115,'DEFEAT')
        break
    else:
        (goneDown, dir, defeat) = change(f, ss, goneDown, dir)
        event = int(button())
        prnt(3,3,str(enemies)+'  ')
        if event==4:
            ss.move(-1)
        elif event==5:
            ss.move(1)
        elif event==6:
            fire(f, ss)
        elif event == 1:
            break
