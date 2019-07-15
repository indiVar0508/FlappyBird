import pygame 
import random

class pipes:
	
	def __init__(self, gameWidth, gameHeight,offset):
		self.pipeLength = 500
		self.pipeBreadth = 70
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		self.top_bottom_y = random.randint(-self.pipeLength + 100,-self.pipeLength + 350)
		self.x = self.gameWidth + offset
		self.space = 150
		self.speed = 5
		self.bottom_top_y = self.top_bottom_y + self.space + self.pipeLength
		self.topPipe = pygame.image.load('Resources\\Pipes\\pipetop.png')
		self.bottomPipe = pygame.image.load('Resources\\Pipes\\pipebottom.png')

	def showPipes(self, gameDisplay):
		gameDisplay.blit(self.topPipe, (self.x, self.top_bottom_y))
		gameDisplay.blit(self.bottomPipe, (self.x, self.bottom_top_y))

	def move(self):
		self.x -= self.speed

	def offScreen(self):
		return self.x < -self.pipeBreadth

	def isdead(self, bird):
		if (bird.y <= self.top_bottom_y + self.pipeLength  or bird.y + bird.height >= self.bottom_top_y) and (bird.x + bird.width > self.x and bird.x < self.x + self.pipeBreadth): return True
		return False

	def reset(self):
		self.top_bottom_y = random.randint(-self.pipeLength + 100,-self.pipeLength + 350)
		self.x = self.gameWidth + (self.gameWidth // 10) + 50
		self.bottom_top_y = self.top_bottom_y + self.space + self.pipeLength



