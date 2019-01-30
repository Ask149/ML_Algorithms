## ML Algorithms ##
    1. KNN
    2. Linear Regression
    3. Particle Swarm Optimization
### 1. K Nearest Neighbor <br> ###
### 2. Linear Regression <br> ###
### 3. Particle Swarm Optimization<br> ###
Particle Swarm Optimization (PSO) is a metaheuristic based optimization algorithm for finding global optimal solution of a function. Here, the particles are considered as solutions to the function, which are randomly initialized. The algorithm iteratively converges to a globally optimal solution. Each particle in the population keeps track of its current position and the best solution it has encountered, called ``pos_bst``. <br><br>
![Swarm](/imgs/swarm.jpg)<br><br>
Each particle has an associated velocity used to traverse the search space. The swarm keeps track of the overall best solution, called ``swarm_pos_bst``. In each iteration of the swarm updates the velocity of the particle toward a weighted sum of the ``pos_bst`` and ``swarm_pos_bst``. The velocity of the particle is then added to the position of the particle and the particle is influenced to travel in a optimal direction with updated velocity. <br><br>
At every iteration in PSO, the position ``x`` and velocity ``v`` of a particle is changed, based on following equations: <br><br>
- ![first equation](https://latex.codecogs.com/gif.latex?x_%7Bk&plus;1%7D%5E%7Bi%7D%20%3D%20x_%7Bk%7D%5E%7Bi%7D%20&plus;%20v_%7Bk&plus;1%7D%5E%7Bi%7D)<br><br>
- ![second equation](https://latex.codecogs.com/gif.latex?v_%7Bk&plus;1%7D%5E%7Bi%7D%20%3D%20w_%7Bk%7D%20v_%7Bk%7D%5E%7Bi%7D%20&plus;%20c_%7B1%7Dr_%7B1%7D%28p_%7Bk%7D%5E%7Bi%7D%20-%20x_%7Bk%7D%5E%7Bi%7D%29%20&plus;%20c_%7B2%7Dr_%7B2%7D%28p_%7Bk%7D%5E%7Bg%7D%20-%20x_%7Bk%7D%5E%7Bi%7D%29)<br><br>
#### Executing the code ####
- Clone this repository:
```
git clone https://github.com/ask149/ML_Algorithms
```
- Run the code:
```
cd ML_Algorithms/<algorithm-name>
python3 <file-name>.py
```

### References ###
- [Particle Swarm Optimization](https://ieeexplore.ieee.org/document/488968).
