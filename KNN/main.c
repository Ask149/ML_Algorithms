#include <stdio.h>

struct Point{
	double amplitude;
	double distance;
	int label;
};

int classifyPoint(struct Point arr[], int n, int k, struct Point p){
	
	// Calulate the distance
	for(int i=0;i<n;i++){
		arr[i].distance = ( arr[i].amplitude - p.amplitude);
		if(arr[i].distance<0){
			arr[i].distance = -1*arr[i].distance;
		}
	}

	// Bubble Sort 
	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			if(arr[i].distance>arr[j].distance){
				struct Point temp;
				temp.amplitude = arr[i].amplitude;
				temp.label = arr[i].label;
				temp.distance = arr[i].distance;

				arr[i].amplitude = arr[j].amplitude;
				arr[i].label = arr[j].label;
				arr[i].distance = arr[j].distance;

				arr[j].amplitude = temp.amplitude;
				arr[j].label = temp.label;
				arr[j].distance = temp.distance;
			}
		}
	}

	// Initilize the frequency count of the nearest labels
	int freq[4];
	for(int i=0;i<4;i++)
	{
		freq[i]=0;	
	}

	for(int i=0;i<k;i++){
		for(int j=0;j<4;j++){
			if(arr[i].label==j){
				freq[j]++;
				break;
			}
		}
	}

	int index = 0;
	int max1 = -1;

	// Find the label with maximum frequency
	for(int i=0;i<4;i++){
		if(max1 < freq[i]){
			index=i+1;
			max1 = freq[i];
		}
	}
	return index;
}
int main(){
    int n = 17; // Number of data points 
    struct Point arr[n]; 
  
    arr[0].amplitude = 1; 
    arr[0].label = 0; 
  
    arr[1].amplitude = 2; 
    arr[1].label = 0; 
  
    arr[2].amplitude = 5; 
    arr[2].label = 1; 
  
    arr[3].amplitude = 3; 
    arr[3].label = 1; 
  
    arr[4].amplitude = 3; 
    arr[4].label = 2; 
  
    arr[5].amplitude = 1.5; 
    arr[5].label = 2; 
  
    arr[6].amplitude = 7; 
    arr[6].label = 3; 
  
    arr[7].amplitude = 6; 
    arr[7].label = 3; 
  
    arr[8].amplitude = 3.8; 
    arr[8].label = 1; 
  
    arr[9].amplitude = 3; 
    arr[9].label = 0; 
  
    arr[10].amplitude = 5.6; 
    arr[10].label = 2; 
  
    arr[11].amplitude = 4; 
    arr[11].label = 3; 
  
    arr[12].amplitude = 3.5; 
    arr[12].label = 0; 
  
    arr[13].amplitude = 2; 
    arr[13].label = 0; 
  
    arr[14].amplitude = 2; 
    arr[14].label = 1; 
  
    arr[15].amplitude = 2; 
    arr[15].label = 2; 
  
    arr[16].amplitude = 1; 
    arr[16].label = 3; 
  
    /*Testing Point*/
    struct Point p; 
    p.amplitude = 2.5; 
    printf("%d",classifyPoint(arr,n,4,p));
 }