# read train data from .txt files
def readTrainData():
  with open('train_x.txt') as f:
    train_x = f.readlines()
  train_x = [int(i.strip()) for i in train_x]
  
  with open('train_y.txt') as f:
    train_y = f.readlines()
  train_y = [int(i.strip()) for i in train_y]

  return train_x,train_y

# for line y = ax + b
def fit(train_x,train_y,a,b,epochs,rate):
  error =0
  a_min = a
  b_min = b
  epoch = 0
  for index in range(len(train_x)):
    error = error + (((a*train_x[index]+b) - train_y[index])/len(train_x))
  error_min = error/len(train_x)

  while epoch<epochs:
    error = 0
    epoch = epoch+1
    error_total_b = 0    
    error_total_a = 0
    for index in range(len(train_x)):
      error = ( (a*train_x[index]+b) - train_y[index] )/len(train_x)
      error_total_b = error_total_b + error
      error_total_a = error_total_a + error*train_x[index]/len(train_x)
    a = a-2*rate*error_total_a/len(train_x)
    b = b-2*rate*error_total_b/len(train_x)
    if abs(error_min) > abs(error_total_b):
      error_min = error_total_b
      a_min = a
      b_min = b
  return a_min,b_min

def error(train_x,train_y,a,b):
  error = 0.00
  for i in range(len(train_y)):
    error += abs((a*train_x[i]+b)-train_y[i])
    error = float(error/len(train_y))
  return error

def predict(x,a,b):
  return (a*x+b)