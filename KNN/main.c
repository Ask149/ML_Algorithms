#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void printElementOfLabel(double amplitude[], int labels[],int n,int label){
	printf("Elements of Label : %d\n",label+1);
	for(int i=0;i<n;i++){
		if(labels[i]==label){
			printf("%f ",amplitude[i]);
		}
	}
	printf("\n");
}

int classifyPoint(double amplitude[], double distance[] ,int label[], int n, int k, int p, double test){
	
	// Calulate the distance
	for(int i=0;i<n;i++){
		distance[i] = ( amplitude[i] - test);
		if(distance[i]<0){
			distance[i] = -1*distance[i];
		}
	}

	for(int i=0;i<k;i++)
	{
		printElementOfLabel(amplitude,label,n,i);
	}

	// Initilize the frequency count of the nearest labels
	int freq[k];
	for(int i=0;i<4;i++)
	{
		freq[i]=0;	
	}

	int min_element = distance[n-1];
	int min_index = n-1;
	
	// Sort the Top p elements in the list by distance in ascending order
	for(int j=n-1;j>=n-p;j--){
		for(int i=0;i<=j;i++){
			if(distance[i]<min_element){
				min_element = distance[i];
				min_index = i;
			}
		}

		double temp1 = min_element;
		distance[min_index]=distance[j];
		distance[j] = temp1;

		temp1 = amplitude[min_index];
		amplitude[min_index]=amplitude[j];
		amplitude[j] = temp1;

		int temp2 = label[min_index];
		label[min_index] = label[j];
		label[j] = temp2; 

		min_index = j-1;
		min_element = distance[j-1];
	}

	for(int i=n-1;i>=n-p;i--){
		//printf("A = %f, D = %f , L = %d\n",amplitude[i], distance[i], label[i] );
		for(int j=0;j<k;j++){
			if(label[i]==j){
				freq[j]++;
				break;
			}
		}
	}

	int index = 0;
	int max1 = -1;

	// Find the label with maximum frequency
	for(int i=0;i<k;i++){
		//printf("freq[%d] = %d\n", i+1, freq[i]);
		if(max1 < freq[i]){
			index=i+1;
			max1 = freq[i];
		}
		else if(max1 == freq[i]){
			//printf("Same max freq as %d is %d = %d \n",i+1, index , freq[i]);
		}
	}
	return index;
}
int main(){
    srand(time(0));
    printf("Hello\n");
    int n = (int)rand()%(20+1-10)+10; // Number of data points 
	double amplitude[n];
  	double distance[n];
  	int label[n];
  	srand(time(0));
  	int k = rand()%(5-1+1)+1; // Number of classes
  	int upper_limit = (k); 
  	if(upper_limit>(n/k+1))
  		upper_limit = (n/k+1);
  	srand(time(0));
  	int p = rand() % ( upper_limit+1 - 2 ) + 2;
	
  	for(int i=0;i<n;i++){
  		amplitude[i] = rand() % (((n+1)*i+n) + 1 - ((n+1*i)-n)) + ((n+1*i)-n);
  		label[i] = rand() % (k - 0) + 0;
  	}

    /*Testing Point*/
    double testpoint = rand()% ((n+1)*(n+1));
    
    printf("n = %d,k = %d,p = %d, test point = %f\n",n,k,p,testpoint);
    printf("Predicted Label : %d\n",classifyPoint(amplitude,distance,label,n,k,p,testpoint));
 }