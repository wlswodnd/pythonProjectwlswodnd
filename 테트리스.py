import sys
from math import sqrt
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN,\
    K_LEFT,K_RIGHT,K_DOWN,K_SPACE

BlOCK_DATA = (
  (
    (0,0,1,
     1,1,1,
     0,0,0),
    (0,1,0,
     0,1,0,
     0,1,1),
    (0,0,0,
     1,1,1,
     1,0,0),
    (1,1,0,
     0,1,0,
     0,1,0),
 ),(
    (2,0,0,
     2,2,2,
     0,0,0),
    (0,2,2,
     0,2,0,
     0,2,0),
    (0,0,0,
     2,2,2,
     0,0,2),
    (0,2,0,
     0,2,0,
     2,2,0)
 ),(
    (0,3,0,
     3,3,3,
     0,0,0),
    (0,3,0,
     0,3,3,
     0,3,0),
    (0,0,0,
     3,3,3,
     0,3,0),
    (0,3,0,
     3,3,0,
     0,3,0)
),(
    (4,4,0,
     0,4,4,
     0,0,0),
    (0,0,4,
     0,4,4,
     0,4,0),
    (0,0,0,
     4,4,0,
     0,4,4),
    (0,4,0,
     4,4,0,
     4,0,0)
),(
    (0,5,5,
     5,5,0,
     0,0,0),
    (0,5,0,
     0,5,5,
     0,0,5),
    (0,0,0,
     0,5,5,
     5,5,0),
    (5,0,0,
     5,5,0,
     0,5,0)
),(
    (6,6,6,6),
    (6,6,6,6),
    (6,6,6,6),
    (6,6,6,6),
),(
    (0,7,0,0,
     0,7,0,0,
     0,7,0,0,
     0,7,0,0),
    (0,0,0,0,
     7,7,7,7,
     0,0,0,0,
     0,0,0,0),
    (0,0,7,0,
     0,0,7,0,
     0,0,7,0,
     0,0,7,0),
    (0,0,0,0,
     0,0,0,0,
     7,7,7,7,
     0,0,0,0)
    )
)

class Block:
    """ 블록 객체 """
    def __init__(self,count):
        self.turn = randint(0,3)
        self.type = BlOCK_DATA[randint(0,6)]
        self.data = self,type[self.turn]
        self.size = int(sqrt((len(self.data))))
        self.xpos = randint(2,8-self.size)
        self.ypos = 1-self.size
        self.fire = count + INTERVAL

    def updata(self,count):
        """ 블럭 상태 갱신 (소거한 단언 수를 반환한다) """
        # 아래로 충돌!
        erased = 0
        if is_overlapped(self.xpos,self.ypos *1 , self.turn):
            for y_effset in range(Block.size):
                for x_effset in range(Block.size):
                    if 0 <= self.xpos+x_effset <  WIDTH and \
                        0 <= self.ypos+y_effset < HIGHT:
                        val = Block.data[y_effset*Block.size \
                                            + x_effset]
                        if val != 0:
                            FIELD[self.ypos+y_effset]\
                                 [self.xpos+x_effset] = val

            go_next_block(count)

        if self.fire < count:
            self.fire = count + INTEVAL
            self.ypos += 1
        return erased

    def drew(self):
        """블록을 그린다"""
        for index in range(len(self.data)):
            xpos = index % self.size
            ypos = index // self.size
            val = self.data[index]
            if 0 <= ypos + self.ypos < HIGHT and \
                0 <= xpos + self.xpos < WIDTH and val != 0:
                xpos = 25 + (xpos + self.xpos) * 25
                ypos = 25 + (ypos + self.ypos) * 25
                pygame.draw.rect(SURFACE, COLORS[val],
                                 (xpos, ypos, 24, 24))

def is_game_over():
    """ 게임 오버인지 아닌지 """
    filled = 0
    for cell in FIELD[0]:
        if cell != 0:
            filled += 1
    return filled > 2   # 2 = 좌우의 벽

def go_next_block(count):
    """ 다음 블럭으로 전환한다"""
    global Block, NEXT_BLOCK
    Block = NEXT_BLOCK if NEXT_BLOCK != None else Block(count)
    NEXT_BLOCK = Block(count)

def is_overlapped(xpos, ypos, turn):
    """ 블럭이 벽이나 땅의 블럭과 충돌하는지 아닌지 """
    data = Block.type[turn]
    for y_effset in range(Block.size):
        for x_effset in range(Block.size):
            if 0 <= xpos+x_effset < WIDTH and \
                0 <= ypos+y_effset < HIGHT:
                if data[y_effset+Block.size + x_effset] != 0 and \
                    FIELD[ypos+y_effset][xpos+x_effset] != 0:
                    return True
    return False

# 전역 변수
pygame.init()
pygame.key.set_repeat(30,30)
SURFACE = pygame.display.set_mode([600,600])
FPSCLOCK = pygame.time.Clock()
WIDTH = 12
HIGHT = 22
INTERVAL = 40
FIELD = [[0 for _ in range(WIDTH)] for _ in range(HIGHT)]
COLORS = ((0,0,0),(255,165,0),(0,0,255),(0,255,255), \
          (0,255,0),(255,0,255),(255,255,0),(255,0,0),(120,120,120))
Block = None
NEXT_BLOCK = None

def main():
    """ 메인 루틴 """
    global INTEVAL
    count = 0
    score = 0
    gamw_over = False
    smallfont = pygame.font.SysFont(None, 36)
    Largefont = pygame.font.SysFont(None, 72)
    mwssage_over = Largefont.render("GAME OVER!!",
                                    True,(0,255,255))
    mwssage_rect = mwssage_over.get_rect()
    mwssage_rect.center = (300,300)

    go_next_block(INTEVAL)

    for ypos in range(HIGHT):
        