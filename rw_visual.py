import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new RWs until conditions met
active = True
while active:

	# Initialize the randomwalk
	rw = RandomWalk(num_points=50_000)
	rw.fill_walk()

	# Set the style and plots
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(20, 12), dpi=256)
	# Scatter plot the random walks
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_value, rw.y_value, s=1, c=point_numbers, cmap=plt.cm.Blues,
	           edgecolors='none')

	# Emphasize the starting and ending points
	ax.scatter(0, 0, c='black', s=50, edgecolors='none')
	ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', s=50, edgecolors='none')

	# Set the axes
	ax.set_aspect('equal')
	ax.set_title('Random Walk Visual')
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n)")
	if keep_running == 'n':
		active = False
