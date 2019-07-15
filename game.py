from Pipes import *
import time
import numpy as np
from Bird import *

class flappyBird:
	def __init__(self):
		pygame.init()
		self.Backgrounds = [ 'Sky.png'  ] #'WinterMountain.png', 'Mountain.png', 'Basic.png'
		self.gameWidth = 350
		self.indexBackground = random.randint(0, len(self.Backgrounds)-1)
		self.gameHeight = 500
		self.gameDisplay = pygame.display.set_mode((self.gameWidth, self.gameHeight))
		pygame.display.set_caption('FlappyBird')
		self.background = pygame.image.load('Resources\\Backgrounds\\background'+self.Backgrounds[self.indexBackground])
		self.fps = pygame.time.Clock()
		self.score = 0
		self.frameRate = 50
		self.bird = Bird(self.gameWidth, self.gameHeight) 
		self.pipes = [pipes(self.gameWidth, self.gameHeight,50),pipes(self.gameWidth, self.gameHeight,300)]

	def makeobjMsg(self, msg, fontD,color = (0, 0, 0)):
		return fontD.render(msg, True, color), fontD.render(msg, True, color).get_rect()
        
	def message(self, msg, color = (0, 0, 0), fontType = 'freesansbold.ttf', fontSize = 15, xpos = 10, ypos = 10):
		fontDefination = pygame.font.Font(fontType, fontSize)
		msgSurface, msgRectangle = self.makeobjMsg(msg, fontDefination, color)
		msgRectangle = (xpos, ypos)
		self.gameDisplay.blit(msgSurface, msgRectangle)

	def closestPipe(self, bird):
		thePipe = self.pipes[0]
		x = self.gameWidth
		for pipe in self.pipes:
			if bird.x < pipe.x + pipe.pipeBreadth + 0.00001:
				if abs(pipe.x + pipe.pipeBreadth - bird.x) < x: 
					thePipe = pipe
					x = abs(pipe.x + pipe.pipeBreadth - bird.x)
		return thePipe

	def pauseGame(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_s:
						return
			self.gameDisplay.fill((51, 51, 51))
			self.message(msg = 'Press S to start.!',color = (255, 255, 255), fontSize = 30, xpos = self.gameWidth // 2 - 120, ypos = self.gameHeight // 2)
			pygame.display.update()

	def play(self):
		# move = 0.0

		while not self.bird.dead:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE: self.bird.jump()

#pygame.draw.line(gameDisplay, (255, 255, 255),(self.x, self.y), (px, py),width = 1 )

			self.gameDisplay.blit(self.background, (0, 0))
			self.bird.showBird(self.gameDisplay)
			self.bird.fall()
			self.fps.tick(self.frameRate)
			self.message(msg = 'score : ' + str(self.score))
			for pipe in self.pipes: pipe.showPipes(self.gameDisplay)
			for pipe in self.pipes: pipe.move()
			for pipe in self.pipes: 
				if pipe.offScreen():
					pipe.reset()
			someOneCrossed = 0
			pipe = self.closestPipe(self.bird)
			if pipe.isdead(self.bird):  
				self.bird.dead = True
			pygame.draw.line(self.gameDisplay, (255, 0, 0),(self.bird.x, self.bird.y), (pipe.x + pipe.pipeBreadth, pipe.bottom_top_y))
			pygame.draw.line(self.gameDisplay, (0, 0, 255),(self.bird.x, self.bird.y), (pipe.x + pipe.pipeBreadth, pipe.top_bottom_y + pipe.pipeLength))
			pygame.draw.line(self.gameDisplay, (0, 0, 0),(self.bird.x, self.bird.y), (pipe.x, self.bird.y))
					# pygame.draw.line(self.gameDisplay, (100, 10, 1),(bird.x, bird.y), (bird.x, 0),5)
					# pygame.draw.line(self.gameDisplay, (1, 10, 100),(bird.x, bird.y), (bird.x, self.gameHeight),5)
					# pygame.display.flip() 
					# print(bird.x , pipe.x + pipe.pipeBreadth,bird.x > pipe.x + pipe.pipeBreadth)
			if self.bird.x >= (pipe.x + pipe.pipeBreadth):
				someOneCrossed = 1
			if someOneCrossed == 1: self.score += 1
			pygame.display.update()
			pygame.display.flip() 
			# print('dead')

if __name__ == '__main__':
	game = flappyBird()
	game.pauseGame()
	game.play()