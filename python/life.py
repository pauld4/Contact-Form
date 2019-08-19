# Conway's Game of Life
# Last update: August 18, 2019
# By Paul Dziedzic https://www.websitesbypaul.com
#
# The current program prints a grid of squares
# and a square can be toggled by clicking on it
#
# CONTROLS
# Press ESC to close
# Press SPACE to step forward
#
# Rules:
# Squares can be "live" (1) or "dead" (0)
# 1. A square with less than 2 adjacent live squares will die
# 2. A square with 2 or 3 adjacent live squares will be okay, and will not be affected
# 3. A square with 4 or more live squares will die
# 4. A dead square with exactly 3 adjacent live squares will come to life

import pygame, random
from pygame.locals import *

class app:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.width, self.height = 640, 400
		self.board = board()
		
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
			elif event.key == K_SPACE:
				self.board.goStep()

	def on_loop(self):
		pass

	def on_render(self):
		self.background.fill((120,20,54))
		for row in self.board.squares:
			for sq in row:
				if sq.val == 0:
					color = (90,90,90)
				else:
					color = (125,125,125)
				pygame.draw.rect(self.background, (color), (sq.posx*(sq.size + 1), sq.posy*(sq.size + 1), sq.size, sq.size))
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
	def __init__(self,size):
		self.posx = 0
		self.posy = 0
		self.size = size
		self.val = 0
	def toggle(self):
		if self.val == 0:
			self.val = 1
		else:
			self.val = 0
	def getPos(self):
		return (self.posx,self.posy)

class board:
	def __init__(self):
		self.axis_x = 20
		self.axis_y = 20
		self.squares = [[0] * self.axis_y for i in range(self.axis_x)]
		self.turn = 0

		for x in range(0,self.axis_x):
			for y in range(0,self.axis_y):
				sq = square(16)
				sq.posx = x
				sq.posy = y
				self.squares[x][y] = sq

	def tickPos(self,pos):
		x = int(pos[0] / 17) # Convert coordinate from mouse to index number
		y = int(pos[1] / 17)
		if x < self.axis_x and y < self.axis_y:
			if x >= 0 and y >= 0:
				self.squares[x][y].toggle()

	def getAdjSq(self,pos):
		adjCount = 0
		sq = self.squares[pos[0]][pos[1]] # Get the square to reference
		#print("You clicked {}, {}".format(pos[0],pos[1]))
		for x in range(sq.posx - 1, sq.posx + 2):
			for y in range(sq.posy - 1, sq.posy + 2):
				if x < self.axis_x and y < self.axis_y: # Filter out numbers outside of the grid
					if x >= 0 and y >= 0: # And negative numbers that cannot be in an array
						if x != pos[0] or y != pos[1]: # Not the square that was clicked on
							#print("Checking {}, {}".format(x,y))
							if self.squares[x][y].val == 1: # If the square is live, add it to the count
								adjCount += 1

		return adjCount

	def goStep(self):
		self.turn += 1
		toggle_list = [] # Since the squares need to be toggled all at once, we can add them to a queue
		for x in range(0, self.axis_x):
			for y in range(0, self.axis_y): # Go through all the squares // todo: shorten to only "live" squares, and their adjacent squares
				sq = self.squares[x][y] # Load the square
				adjCount = self.getAdjSq((x,y))
				if sq.val == 0 and adjCount == 3: # Rule #4
					toggle_list.append(sq)
				elif sq.val == 1:
					if adjCount <= 1: # Rule #1
						toggle_list.append(sq)
					elif adjCount >= 4: # Rule #3, rule #2 is applied to the rest of the live squares (nothing happens)
						toggle_list.append(sq)

		for sq in toggle_list: # Toggle the squares
			sq.toggle()
			
if __name__ == "__main__":
	life = app()
	life.on_execute()