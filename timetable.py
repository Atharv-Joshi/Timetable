import numpy as np
import random as rd


entered_sub = []
arr = np.zeros((5,5))
arr = arr.astype(np.object)


sub_dict = {1 : 'pps', 2 : 'phy', 3 : 'bee', 4 : 'sme', 5: 'M1'}
sub_dict_keys = list(sub_dict.keys())



mt = ['A','B','C','D','E']
st = ['a','b','c','d','e']


def r_list_generator(sub_dict_keys,entered_sub):
	while(len(entered_sub) <= 4):
		temp = rd.choice(sub_dict_keys)
		if temp in entered_sub:
			pass
		else:
			entered_sub.append(temp)
	return(entered_sub)



entered_sub = r_list_generator(sub_dict_keys,entered_sub)
print(entered_sub)



for i in range(5):
	m,n = i,i
	for j in range(5):
		
		if ( j == n):
			arr[i,j] = sub_dict[entered_sub[0]]
		if (j == n+1):
			arr[i,j] = sub_dict[entered_sub[1]]
		if (j == n+2):
			arr[i,j] = sub_dict[entered_sub[2]]	
		if (j == n+3):
			arr[i,j] = sub_dict[entered_sub[3]]
		if (j == n+4):
			arr[i,j] = sub_dict[entered_sub[4]]			
		
		if (j == n-1):
			arr[i,j] = sub_dict[entered_sub[4]]
		if (j == n-2):
			arr[i,j] = sub_dict[entered_sub[3]]
		if (j == n-3):
			arr[i,j] = sub_dict[entered_sub[2]]			
		if (j == n-4):
			arr[i,j] = sub_dict[entered_sub[1]]		
print(arr)



