from particle import Particle

class PSO():
	def __init__(self, cost, pos_0, bound, particles, maxiter):
		global dimensions
		dimensions = len(pos_0)
		swarm_err_bst = -1        # minimum error for group
		swarm_pos_bst = []        # best position for group

		# swarm of particles
		swarm = []
		for i in range(0,particles):
			swarm.append(Particle(pos_0,dimensions))

		i=0
		while i < maxiter:        # optimization loop
			for j in range(0,particles):        # evaluate fitness of particles
				swarm[j].evaluate(cost,dimensions)

				# check whether the current particle is the best in swarm and update the best
				if swarm[j].err < swarm_err_bst or swarm_err_bst == -1:
					swarm_pos_bst = list(swarm[j].pos)
					swarm_err_bst = float(swarm[j].err)

      # update velocities and positions of the particles
			for j in range(0,particles):
				swarm[j].vel_update(swarm_pos_bst,dimensions)
				swarm[j].pos_update(bound,dimensions)
			i+=1

		# print result
		print('Final : '+str(swarm_pos_bst)+' '+str(swarm_err_bst))