from bird.AIBird import AIBird as Bird
import numpy as np

class Population:

	def __init__(self, windowWidth, windowHeight, layers ,mutation = 0.1, populationSize = 50):
		self.populationSize = populationSize
		self.windowWidth = windowWidth
		self.windowHeight = windowHeight
		self.mutation = mutation
		self.birds = [Bird(self.windowWidth, self.windowHeight, layers) for _ in range(self.populationSize)]
		self.generation = 0
		self.matingPool = []
		self.bestFitness = 0
		self.bestBird = None
		self.total = 0.0
		self.alive = self.populationSize


	def allDead(self):
		for bird in self.birds:
			if not bird.dead: return False
		return True


	def evolve(self):
		self.computeFitness()
		self.naturalSelection()
		self.generate()

	def generate(self):
		self.birds = []
		for _ in range(self.populationSize):
			p1, p2 = self.matingPool[np.random.randint(0,len(self.matingPool)-1)], self.matingPool[np.random.randint(0,len(self.matingPool)-1)]
			child = p1.biCrossOver(p2)
			# p1 = self.matingPool[np.random.randint(0,len(self.matingPool)-1)]
			# child = p1.uniCrossOver()
			child.brain.mutate(mutationRate = self.mutation)
			self.birds.append(child)
		self.generation+=1


	def naturalSelection(self):
		self.matingPool = []
		maxFit = self.birds[0].fitness
		# print('first',maxFit)
		for bird in self.birds:
			if bird.fitness > maxFit: 
				maxFit = bird.fitness
		# print('best',maxFit)
		for bird in self.birds:
			score = int((bird.fitness / maxFit) * 100)
			while score > 0:
				self.matingPool.append(bird)
				score -= 1


	def computeFitness(self):
		self.bestFitness = 0
		for bird in self.birds: 
			fitn = bird.getFitness()
			self.total += fitn
			# print(fitn)
			if fitn > self.bestFitness: 
				self.bestFitness = fitn
				self.bestBird = bird
		# print(self.generation,' -> ', self.bestFitness)


	# def pickSomeone(self):
	# 	index = np.random.randint(0, self.populationSize-1)
	# 	r = np.random.rand()
	# 	attempts = 0
	# 	while r > 0 and attempts < 100:
	# 		if self.birds[index].probability>0: r -= self.birds[index].probability
	# 		else: self.birds[index].probability
	# 		index = (index + 1) % self.populationSize
	# 		attempts += 1
	# 	if r<= 0: return self.birds[index - 1]
	# 	else: return self.birds[1]

	# def generate(self):
	# 	matingPool = []
	# 	for bird in self.birds: 
	# 		bird.probability = bird.fitness / self.total
	# 		# print(bird.probability)
	# 	while len(self.birds) != len(matingPool):
	# 		parentOne = self.pickSomeone()
	# 		# parentTwo = self.pickSomeone()
	# 		# child = parentOne.biCrossOver(parentTwo)
	# 		child = parentOne.uniCrossOver()
	# 		child.brain.mutate(mutationRate = self.mutation)
	# 		matingPool.append(child)
	# 	self.birds = np.copy(matingPool)
	# 	self.generation += 1
	# 	self.total = 0