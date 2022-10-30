import pygame
from Population import Population
from pipes import Pipes
from game import flappyBird
import numpy as np

class flappyBirdAI(flappyBird):
    def __init__(self):
        super().__init__()
        self.bestScore = 0
        self.population = Population(self.gameWidth , self.gameHeight,layers = [5, 8, 2], mutation = 0.05, populationSize = 50)

    def reset(self):
        self.score = 0
        self.population.alive = self.population.populationSize
        self.pipes = [Pipes(self.gameWidth, self.gameHeight,0),Pipes(self.gameWidth, self.gameHeight,250)]
        self.gameDisplay.blit(self.background, (0, 0))
        for bird in self.population.birds:
            bird.showBird(self.gameDisplay)

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

        while not self.population.allDead():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                    

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return False
                    if event.key == pygame.K_SPACE:
                        for bird in self.population.birds: 
                            if not bird.dead: bird.jump()

    #pygame.draw.line(gameDisplay, (255, 255, 255),(self.x, self.y), (px, py),width = 1 )

            for bird in self.population.birds: 
                if not bird.dead:
                    pipe = self.closestPipe(bird)
                    action = bird.brain.feedForward(np.array([[((pipe.top_bottom_y + pipe.pipeLength) / self.gameHeight), (bird.y / self.gameHeight), (pipe.bottom_top_y / self.gameHeight), bird.move,  ((pipe.x - bird.x) / self.gameWidth)]]).transpose(), predict = True, _round = False).ravel()
                    # action = bird.brain.feedForward(np.array([[bird.y, pipe.top_bottom_y + pipe.pipeLength, pipe.bottom_top_y, bird.move, abs(pipe.x - bird.x)]]).transpose(), predict = True, _round = False).ravel()
                    # print(np.array([[(bird.y / self.gameHeight), ((pipe.top_bottom_y + pipe.pipeLength) / self.gameHeight), (pipe.bottom_top_y / self.gameHeight), move, (abs(pipe.x - bird.x) / self.gameWidth)]]))
                    # print(action)
                    # print(np.array([[bird.y, pipe.top_bottom_y + pipe.pipeLength, pipe.bottom_top_y, move, abs(pipe.x - bird.x)]]))

                    if action[0] > action[1]: 
                        self.population.alive -= bird.jump()
                        bird.move = 1.0
                    else: bird.move = 0.0

            # quit()
            self.gameDisplay.blit(self.background, (0, 0))
            for bird in self.population.birds:
                if not bird.dead: 
                    bird.fitness += 0.01
                    bird.showBird(self.gameDisplay)
            self.fps.tick(self.frameRate)
            self.message(msg = 'score : ' + str(self.score))
            self.message(msg = 'Best Score : ' + str(self.bestScore),ypos = 28)
            self.message(msg = 'Generation : ' + str(self.population.generation), ypos = 45)
            self.message(msg = 'Alive : ' + str(self.population.alive), ypos = 60)
            for pipe in self.pipes: pipe.showPipes(self.gameDisplay)
            for pipe in self.pipes: pipe.move()
            for pipe in self.pipes:
                for bird in self.population.birds:
                    if not bird.dead:
                        if pipe.isdead(bird):
                            bird.dead = True
                            bird.fitness -=  1.5
                            # bird.fitness -= 1.0
                            self.population.alive -= 1
            for pipe in self.pipes: 
                if pipe.offScreen():
                    pipe.reset()
            someOneCrossed = 0
            for bird in self.population.birds:
                if not bird.dead:
                    pipe = self.closestPipe(bird)
                    pygame.draw.line(self.gameDisplay, (255, 0, 0),(bird.x, bird.y), (pipe.x + pipe.pipeBreadth, pipe.bottom_top_y))
                    pygame.draw.line(self.gameDisplay, (0, 0, 255),(bird.x, bird.y), (pipe.x + pipe.pipeBreadth, pipe.top_bottom_y + pipe.pipeLength))
                    pygame.draw.line(self.gameDisplay, (0, 0, 0),(bird.x, bird.y), (pipe.x, (bird.y)))
                    # pygame.draw.line(self.gameDisplay, (100, 10, 1),(bird.x, bird.y), (bird.x, 0),5)
                    # pygame.draw.line(self.gameDisplay, (1, 10, 100),(bird.x, bird.y), (bird.x, self.gameHeight),5)
                    pygame.display.flip() 
                    # print(bird.x , pipe.x + pipe.pipeBreadth,bird.x > pipe.x + pipe.pipeBreadth)
                    if bird.x >= (pipe.x + pipe.pipeBreadth):
                        bird.fitness += 5
                        someOneCrossed = 1
                    self.population.alive -= bird.fall()
            if someOneCrossed == 1: self.score += 1
                    #self.pipes.append(pipes(self.gameWidth, self.gameHeight))
                    #self.pipes.append(pipes(self.gameWidth,self.gameHeight))
            # for bird in self.population.birds: 
            # 	if not bird.dead: self.population.alive -= bird.fall()
            pygame.display.update()
            pygame.display.flip() 
            # for bird in self.population.birds: print(bird.fitness)
        # quit()
        self.population.evolve()
        if self.score > self.bestScore: self.bestScore = self.score
        self.reset()
        return True



def init_game():
    game = flappyBirdAI()
    game.pauseGame()
    keep_playing = True
    while keep_playing:	
        keep_playing = game.play()

if __name__ == '__main__':
    init_game()