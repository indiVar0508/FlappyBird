import numpy as np

class myNeuralNet:

	def __init__(self, layers = [2, 2, 1], learningRate = 0.09, weights = None, biasses = None,epsilon = None):
		self.layers = layers
		self.learningRate = learningRate
		if not biasses: self.biasses = [np.random.randn(l, 1)  for l in self.layers[1:]]
		else: self.biasses = biasses 
		if not weights: self.weights = [np.random.randn(i, o) for o, i in zip(self.layers[:-1], self.layers[1:])]
		else: self.weights = weights
		self.cost = []
		if epsilon != None: 
			self.epsilon = epsilon
			self.epsilonDecay = 0.95

	def sigmoid(self, z):
		return (1.0 / (1.0 + np.exp(-z)))

	def sigmoidPrime(self, z):
		return (self.sigmoid(z) * (1 - self.sigmoid(z)))

	def mutate(self, mutationRate = 0.01):
		for i in range(len(self.weights)):
			for row in range(len(self.weights[i])):
				for col in range(len(self.weights[i][row])):
					if np.random.random() < mutationRate: self.weights[i][row][col] = np.random.randn()
		for i in range(len(self.biasses)):
			for row in range(len(self.biasses[i])):
					if np.random.random() < mutationRate: self.biasses[i][row] = np.random.randn()

	def giveMeChild(parent):
		return myNeuralNet(layers = parent.layers, learningRate = parent.learningRate, weights = parent.weights, biasses = parent.biasses)

	def tanh(self, z):
		return np.tanh(z)


	def feedForward(self, z, predict = False, _round = True):
		activations = [z]
		for w, b in zip(self.weights, self.biasses): activations.append(self.sigmoid(np.dot(w, activations[-1]) + b))
		# for activation in activations: print(activation)
		if predict: 
			if _round: return np.round(activations[-1])
			return activations[-1]
		return np.array(activations)

	def drawLearningRate(self):
		import matplotlib.pyplot as plt
		plt.plot(np.array(self.cost).reshape(-1, 1))
		plt.show()

	def backPropogate(self, x, y):
		bigDW = [np.zeros(w.shape) for w in self.weights]
		bigDB = [np.zeros(b.shape) for b in self.biasses]
		activations = self.feedForward(x)
		delta = activations[-1] - y
		self.cost.append([- y * np.log(activations[-1]) - (1 - y) * np.log(1 - activations[-1])])

		for l in range(2, len(self.layers) + 1):
			bigDW[-l + 1] = (1 / len(x)) * np.dot(delta, activations[-l].T)
			bigDB[-l + 1] = (1 / len(x)) * np.sum(delta, axis = 1)
			delta = np.dot(self.weights[-l + 1].T, delta) * self.sigmoidPrime(activations[-l]) 

		for w, dw in zip(self.weights, bigDW): w -= self.learningRate * dw
		for b, db in zip(self.biasses, bigDB): b -= self.learningRate *db.reshape(-1, 1)




if __name__ == '__main__':
	nn = myNeuralNet(layers = [2, 3, 3, 2, 1], learningRate = 0.55)
	datasetX = np.array([[1, 1], [0, 1], [1, 0], [0, 0]]).transpose()
	datasetY = np.array([[x ^ y] for x, y in datasetX.T]).reshape(1, -1)
	for _ in range(10000): nn.backPropogate(datasetX, datasetY)
	print(nn.feedForward(np.array([[0, 0]]).transpose(), predict = True))
	print(nn.feedForward(np.array([[1, 0]]).transpose(), predict = True))
	print(nn.feedForward(np.array([[0, 1]]).transpose(), predict = True))
	print(nn.feedForward(np.array([[1, 1]]).transpose(), predict = True))
	nn.drawLearningRate()

