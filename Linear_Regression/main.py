from modules import readTrainData,fit,error,predict

if __name__=="__main__":
	
	x, y = readTrainData()
	
	a, b = fit(x,y,1,6,10000000,0.0001)
	
	print(a,b,error(x,y,a,b))

	for i in range(len(x)):
		print(" For x = "+ str(x[i]) + ", Predicted = " + str(predict(x[i],a,b))+ " where y = "+str(y[i]))