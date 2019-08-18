# Conway's Game of Life
# Last update: August 18, 2019
# By Paul Dziedzic https://www.websitesbypaul.com

# The current program prints a grid of squares
# and a square can be toggled by clicking on it
# Press ESC to close

import pygame, random
from pygame.locals import *

class app:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.board = board()
        self.size = self.width, self.height = 640, 400

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Life")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.size)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.board.tickPos(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.background.fill((120,20,54))
        b = self.board
        for sq in b.squares:
            if sq.val == 0:
                color = (90,90,90)
            else:
                color = (125,125,125)
            pygame.draw.rect(self.background, (color), (sq.posx, sq.posy, 16, 16))
        self._display_surf.blit(self.background, (0,0))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

class square:
    def __init__(self,pos):
        self.posx = pos[0]
        self.posy = pos[1]
        self.val = 0
    def move(self):
        if random.randint(1,10) == 1:
            self.posx += 1
    def toggle(self):
        if self.val == 0:
            self.val = 1
        else:
            self.val = 0
    def getPos(self):
        return (self.posx,self.posy)

class board:
    def __init__(self):
        self.squares = []
        self.axis_x = 10
        self.axis_y = 10
        self.turn = 0

        for x in range(0,self.axis_x):
            for y in range(0,self.axis_y):
                self.squares.append(square((x*17,y*17)))

    def tickPos(self,pos):
        for sq in self.squares:
            if pos[0] >= sq.posx and pos[0] <= sq.posx + 16:
                if pos[1] >= sq.posy and pos[1] <= sq.posy + 16:
                    sq.toggle()

if __name__ == "__main__":
    life = app()
    life.on_execute()