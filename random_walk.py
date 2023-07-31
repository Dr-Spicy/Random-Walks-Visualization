import random

random.seed(1)


class RandomWalk:
	"""A class to generate random walks"""

	def __init__(self, num_points=5_000):
		"""Init attributes of class"""
		self.num_points = num_points

		# All walks start at (0,0)
		self.x_value = [0]
		self.y_value = [0]

	def fill_walk(self):
		"""determins the full seq of points in the walk"""
		# Keep taking steps until the walk reaches the desire length.
		while len(self.x_value) < self.num_points:
			# Decide which direction to go and for how far
			x_direction = random.choice([1, -1])
			x_distance = random.choice(range(0, 5))
			x_step = x_distance * x_direction

			y_direction = random.choice([1, -1])
			y_distance = random.choice(range(0, 5))
			y_step = y_distance * y_direction

			# Rejects move that go nowhere.
			if x_step == 0 and y_step == 0:
				continue

			# Calculate the new position.
			x = self.x_value[-1] + x_step
			y = self.y_value[-1] + y_step

			self.x_value.append(x)
			self.y_value.append(y)