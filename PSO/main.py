#--------------------------------------------------------------------------
#
#	A simple implementation of Particle Swarm Optimization ( with python )
#
#--------------------------------------------------------------------------

from pso import PSO
from particle import Particle

#--------------------------------------------------------------------------
#
# Cost function to optimise
def func(x):
	total = 0
	for i in range(len(x)):
		total += x[i]**2
	return total
#
#--------------------------------------------------------------------------

if __name__ == "__main__":
  initial = [5,5]              #starting location
  bounds = [(-10,10),(-10,10)] #x_min, x_max pair for each particle
  PSO(func,initial,bounds,particles=15,maxiter=30)