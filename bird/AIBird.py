import pygame
import numpy as np
import random
from myNN import myNeuralNet as Brain
from bird.Bird import Bird

class AIBird(Bird):
    def __init__(self, gameWidth, gameHeight, layers):
        super().__init__(gameWidth=gameWidth, gameHeight=gameHeight)
        self.fitness = 0.0
        self.brain = Brain(layers = layers)
        self.move = 0
        self.probability = 0

    # def reset(self):
    # 	self.y = self.gameHeight // 2
    # 	# self.bird = pygame.image.load('Resources\\Characters\\BlueBird.png')
    # 	self.fitness = 0.0
    # 	self.velocity = 0
    # 	self.dead = False
    # 	self.probability = 0


    def jump(self):
        super().jump()
        if self.dead: 
            self.fitness -= 3.5
            return 1
        return 0

    def fall(self):
        super().fall()
        if self.dead: 
            self.fitness -= 3.5
            return 1
        return 0

    def getFitness(self):
        return self.fitness

    def biCrossOver(parentOne, parentTwo):
        child = AIBird(parentOne.x * 10, parentTwo.gameHeight, parentOne.brain.layers)
        for idx, _ in enumerate(child.brain.weights):
            if random.random() < 0.5: child.brain.weights[idx] = np.copy(parentOne.brain.weights[idx])
            else: child.brain.weights[idx] = np.copy(parentTwo.brain.weights[idx])
        for idx, _ in enumerate(child.brain.biasses):
            if random.random() > 0.5: child.brain.biasses[idx] = np.copy(parentOne.brain.biasses[idx])
            else: child.brain.biasses[idx] = np.copy(parentTwo.brain.biasses[idx])
        # quit()

        return child

    def uniCrossOver(parentOne):
        child = Bird(parentOne.x * 10, parentOne.gameHeight, parentOne.brain.layers)
        child.brain.weights = np.copy(parentOne.brain.weights)
        child.brain.biasses = np.copy(parentOne.brain.biasses)
        return child
