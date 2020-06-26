import os
import random
import msvcrt
import time
import intro
###
import outro
###
height=20
width=60
snake=[[(int)(height/2)-1,(int)(width/2)-1]]
direction=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
""" direction is 0,1,2,3 like N E S W """
###
def generateCoin(mat,snake):
    xcoin=random.randint(1,height-2)
    ycoin=random.randint(1,width-2)
    for pair in snake:
        if pair==[xcoin,ycoin]:
            generateCoin(mat,snake)
            return
    mat[xcoin][ycoin]='©'
def moveSnake(mat,snake):
    nextx=snake[0][0]+dx[direction]
    nexty=snake[0][1]+dy[direction]
    mat[ snake[0][0] ][ snake[0][1] ]='■'
    if mat[nextx][nexty]==' ':
        snake.insert(0,[nextx,nexty])
        mat[ nextx ][ nexty ]='@'
        sizeSnake=len(snake)
        mat[ snake[sizeSnake-1][0] ][ snake[sizeSnake-1][1] ]= ' '
        snake.pop()
    elif mat[nextx][nexty]=='©':
        snake.insert(0,[nextx,nexty])
        mat[ nextx ][ nexty ]='@'
        generateCoin(mat,snake)
    else:
        outro.outro()
def makeBorder(mat):
    for i in range(1,width-1):
        mat[0][i]=mat[height-1][i]='═'
    for i in range(1,height-1):
        mat[i][0]=mat[i][width-1]='║'
    mat[0][0]='╔'
    mat[0][width-1]='╗'
    mat[height-1][0]='╚'
    mat[height-1][width-1]='╝'
def printGame():
    os.system('cls' if os.name=='nt' else 'clear')
    moveSnake(mat,snake)
    for i in range(height):
        for j in range(width):
            print (mat[i][j],end='')
        print ("\n",end='')
    print("\n")
    print("Score: "+ str(len(snake)))
###
intro.intro()
mat = [[' ' for x in range(width)] for y in range(height)]
makeBorder(mat)
generateCoin(mat,snake)     
while(1):
    if msvcrt.kbhit():
                dir = msvcrt.getch()
                while msvcrt.kbhit():
                    dir = msvcrt.getch()
                dir=dir.decode('ASCII')
                if dir == 'w':
                    direction = 0
                elif  dir == 'd':
                    direction = 1
                elif dir == 's':
                    direction = 2
                elif dir == 'a': 
                    direction = 3
                else:
                    continue
    if direction%2==0:
        time.sleep(0.15)
    else:
        time.sleep(0.1)
    printGame()
