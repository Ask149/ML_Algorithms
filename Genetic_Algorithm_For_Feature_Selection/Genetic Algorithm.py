
# coding: utf-8

# # Genetic Algorithm for Feature Selection

# ## Import Libraries

# In[16]:


import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

np.random.seed(2019)


# ## Load data

# In[17]:


data = pd.read_csv('mushroom.csv')


# In[18]:


data.head()


# In[19]:


data.describe()


# In[20]:


data.info()


# In[21]:


features = list(data.columns.values)


# In[22]:


for c in data.columns:
    if data[c].dtype =='object':
        enc = LabelEncoder()
        enc.fit(list(data[c].values))
        data[c] = enc.transform(list(data[c].values))


# In[23]:


X = data.iloc[:, :22].values
y = data.iloc[:, 22].values


# In[24]:


len(X[0])


# ## Train test splitting

# In[25]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# ## Classification

# In[26]:


clf = GaussianNB()
clf.fit(X_train,y_train)


# In[27]:


y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)


# In[28]:


accuracy


# In[29]:


data.corr()


# ## Genetic Algorithm Class

# In[43]:


class GA():
    def __init__(self,estimator, numberGenerations, numberBestChromosomes, numberRandomChromosomes, numberChildren, mutationRate):
        self.estimator = estimator
        self.generationAccuracyList = []
        self.generationFeatureList = []
        self.numberGenetations = numberGenerations
        self.numberBestChromosomes = numberBestChromosomes
        self.numberRandomChromosomes = numberRandomChromosomes
        self.numberChildren = numberChildren
        self.mutationRate = mutationRate
        self.sizeChromosomes = (int((self.numberBestChromosomes+self.numberRandomChromosomes)/2)*self.numberChildren)
        
        if int((self.numberBestChromosomes+self.numberRandomChromosomes)/2)*self.numberChildren != self.sizeChromosomes:
            print('LHS = (('+str(self.numberBestChromosomes)+                  ' + '+str(self.numberRandomChromosomes)+')/2)*'+str(self.numberChildren)+' = '+str(int((self.numberBestChromosomes+self.numberRandomChromosomes)/2)*self.numberChildren))
            print('RHS = '+str(self.sizeChromosomes))
            raise ValueError("Unstable population size")
    
    def initializePopulation(self):
        self.maxAccuracy = 0
        self.maxAccuracySubset = [True]*(self.numberFeatures)
        population = []
        for i in range(self.sizeChromosomes):
            chromosomes = np.ones(self.numberFeatures, dtype=np.bool)
            mask = np.random.rand(len(chromosomes))<0.3
            chromosomes[mask] = False
            population.append(chromosomes)
        return population
    
    def fitness(self,population):
        X, y = self.dataset
        localMaxAccuracy = 0
        localMaxAccuracySubset = None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        fitness = []
        for child in population:
            try:
                accuracy = accuracy_score(GaussianNB().fit(X_train[:,child],y_train).predict(X_test[:,child]),y_test)
                accuracy = accuracy
                fitness.append(accuracy)
                if float(accuracy)>float(localMaxAccuracy):
                    localMaxAccuracy = accuracy
                    localMaxAccuracySubset = child
                if float(localMaxAccuracy)>float(self.maxAccuracy):
                    self.maxAccuracy = localMaxAccuracy
                    self.maxAccuracySubset = localMaxAccuracySubset
            except:
                fitness.append(0)
        #print('Local Max Accuracy = ',localMaxAccuracy)
        #print('Local Max Accuracy Subset = ',localMaxAccuracySubset)

        self.generationAccuracyList.append(localMaxAccuracy*100)
        cnt = 0
        for i in range(len(localMaxAccuracySubset)):
            if localMaxAccuracySubset[i] == True:
                cnt+=1
        self.generationFeatureList.append(cnt)
        
        #print('Max Accuracy = ',self.maxAccuracy)
        #print('Max Accuracy Subset = ',self.maxAccuracySubset)
        
        fitness, population = np.array(fitness), np.array(population)
        indx = np.argsort(-1*fitness)
        return list(fitness[indx]),list(population[indx,:])
    
    def selectNextPopulation(self,population):
        populationNext = []
        for i in range(self.numberBestChromosomes):
            populationNext.append(population[i])
        for i in range(self.numberRandomChromosomes):
            populationNext.append(random.choice(population))
        random.shuffle(populationNext)
        return populationNext
    
    def crossover(self,population):
        populationNext = []
        for i in range(int(len(population)/2)):
            for j in range(self.numberChildren):
                child1, child2 = population[i], population[len(population)-1-i]
                child = child1
                mask = np.random.rand(len(child))>0.5
                child[mask] = child2[mask]
                populationNext.append(child)
        return populationNext
    
    def mutate(self,population):
        populationNext = []
        for i in range(len(population)):
            chromosomes = population[i]
            if random.random() < self.mutationRate:
                mask = np.random.rand(len(chromosomes)) < 0.05
                chromosomes[mask] = False
            populationNext.append(chromosomes)
        return populationNext
    
    def generatePopulation(self,population):
        sortedFitness, sortedPopulation = self.fitness(population)
        population = self.selectNextPopulation(sortedPopulation)
        population = self.crossover(population)
        population = self.mutate(population)
        
        self.bestChromosomes.append(sortedPopulation[0])
        self.bestFitness.append(sortedFitness[0])
        self.avgFitness.append(np.mean(sortedFitness))
        return population
    
    def fit(self,attributes,target):
        self.bestChromosomes, self.bestFitness, self.avgFitness = [], [], []
        
        self.numberFeatures = attributes.shape[1]
        self.dataset = attributes,target
        
        population = self.initializePopulation()
        for i in range(self.numberGenetations):
            population = self.generatePopulation(population)
        
        return self
    
    @property
    def supportProp(self):
        return self.bestChromosomes[-1]
    
    def getMaxAccuracySubset(self):
        featureList = []
        for i in range((self.numberFeatures)):
            if self.maxAccuracySubset[i] == True:
                featureList.append(list(data.columns)[i])
        return featureList
    
    def plotFitness(self):
        plt.plot(self.generationAccuracyList, label='Fitness')
        plt.plot(self.generationFeatureList, label='Features')
        #plt.plot(self.avgFitness, label='Average')
        #plt.plot(self.bestFitness, label='Best')
        plt.legend()
        plt.ylabel('Fitness/Number of Features')
        plt.xlabel('Generation')
        plt.show()


# In[44]:


obj = GA(estimator=GaussianNB(), numberGenerations=200,numberBestChromosomes=50, numberRandomChromosomes=20, numberChildren=25, mutationRate=0.1)


# In[45]:


obj.fit(X,y)


# In[46]:


obj.plotFitness()


# In[47]:


print(obj.getMaxAccuracySubset())


# In[48]:


print(obj.maxAccuracy)


# In[49]:


print(len(obj.getMaxAccuracySubset()))

