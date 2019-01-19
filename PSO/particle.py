import random

class Particle:
	def __init__(self,pos_0,dimensions):
		self.pos = []
		self.vel = []
		self.pos_best = []
		self.err_best = -1
		self.err = -1

		for i in range(0,dimensions):
			self.vel.append(random.uniform(-1,1))
			self.pos.append(pos_0[i])

	def evaluate(self,cost,dimensions):
		self.err = cost(self.pos)
		if self.err < self.err_best or self.err_best == -1:
			self.pos_best = self.pos
			self.err_best = self.err

	def vel_update(self,swarm_pos_best,dimensions):
		w = 0.4
		c1 = 1
		c2 = 2
		for i in range(0,dimensions):
			r1 = random.random()
			r2 = random.random()

			vel_c1 = c1*r1*(self.pos_best[i]-self.pos[i])
			vel_c2 = c2*r2*(swarm_pos_best[i]-self.pos[i])
			self.vel[i] = w*self.vel[i] + vel_c1 + vel_c2

	def pos_update(self,bound,dimensions):
		for i in range(0,dimensions):
			self.pos[i] = self.pos[i] + self.vel[i]
			self.pos[i] = min( bound[i][1],self.pos[i] )
			self.pos[i] = min( bound[i][0],self.pos[i] )