from modules import readTrainData,fit
x, y = readTrainData()
a, b = fit(x,y,1,5,10000,0.02)
print(a,b)