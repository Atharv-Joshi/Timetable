import numpy as np
#import random
arr = np.zeros((5,5))
sub = [1,2,3,4,5]
mt = ['A','B','C','D','E']
st = ['a','b','c','d','e']
for i in range(5):
	m,n = i,i
	for j in range(5):
		if ( j ==n):
			arr[i,j] = sub[0]
		if (j == n+1):
			arr[i,j] = sub[1]
		if (j == n+2):
			arr[i,j] = sub[2]	
		if (j == n+3):
			arr[i,j] = sub[3]
		if (j == n+4):
			arr[i,j] = sub[4]			
		
		if (j == n-1):
			arr[i,j] = sub[4]
		if (j == n-2):
			arr[i,j] = sub[3]
		if (j == n-3):
			arr[i,j] = sub[2]			
		if (j == n-4):
			arr[i,j] = sub[1]		
print(arr)