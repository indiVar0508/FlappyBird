import pygame
import random

class Bird:
	def __init__(self, gameWidth, gameHeight):
		self.x = gameWidth // 10
		self.birds = ['YellowBird.png']
		self.indexBird = random.randint(0, len(self.birds)-1)
		self.y = gameHeight // 2
		self.gameHeight = gameHeight
		self.bird = pygame.image.load('Resources/Characters/' + self.birds[self.indexBird])
		self.gravity = 7
		self.antiGravity = -60
		self.velocity = 0
		self.height = 20
		self.angle = 0
		self.width = 20
		self.dead = False

	def showBird(self,gameDisplay):
		gameDisplay.blit(self.bird, (self.x, self.y))

	def jump(self):
		self.velocity = self.antiGravity
		self.y += self.velocity
		if(self.y < 0):
			self.dead = True

	def fall(self):
		self.velocity = self.gravity*0.7
		self.y += self.velocity
		self.bird = pygame.transform.rotate(self.bird, -self.angle)
		if self.y + 24  > self.gameHeight:
			self.y = self.gameHeight - 24
			self.dead = True
