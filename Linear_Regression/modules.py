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
  for index in range(0,8):
    error = error + (((a*train_x[index]+b) - train_y[index])/8)
  error_min = error/8

  while epoch<epochs:
    error = 0
    epoch = epoch+1
    error_total_b = 0    
    error_total_a = 0
    for index in range(0,8):
      error = ( (a*train_x[index]+b) - train_y[index] )/8
      error_total_b = error_total_b + error
      error_total_a = error_total_a + error*train_x[index]/10
    a = a-2*rate*error_total_a/8
    b = b-2*rate*error_total_b/8
    if abs(error_min) > abs(error_total_b):
      error_min = error_total_b
      a_min = a
      b_min = b
  return a_min,b_min