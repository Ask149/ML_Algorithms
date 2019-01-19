from modules import readTrainData,fit

if __name__=="__main__":
	
	x, y = readTrainData()
	
	a, b = fit(x,y,1,5,10000,0.02)
	
	print(a,b)