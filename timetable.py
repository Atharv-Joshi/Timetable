#importing required packages
import numpy as np
import random as rd
import pandas as pd


#declaring the required variables
column_dimensions = 5
row_dimensions = 5
filename = 'database1.csv'

#declaring required arrays
entered_sub = []
arr = np.zeros((row_dimensions,column_dimensions))
arr = arr.astype(np.object)
headers = ['hour1','hour2','hour3','hour4','hour5']

#declaring dictionary containg the subject names
sub_dict = {1 : 'pps', 2 : 'phy', 3 : 'bee', 4 : 'sme', 5: 'M1'}
sub_dict_keys = list(sub_dict.keys())


#array  containing teacher names
main_teachers = ['A','B','C','D','E']
substitute_teachers = ['a','b','c','d','e']


#function which randomizes the keys in the subject dicitionary
def r_list_generator(sub_dict_keys,entered_sub):
	while(len(entered_sub) <= 4):
		temp = rd.choice(sub_dict_keys)
		if temp in entered_sub:
			pass
		else:
			entered_sub.append(temp)
	return(entered_sub)


#assigning the subjects to the array cells
def subject_assigner(sub_dict,entered_sub,arr):
	for i in range(row_dimensions):
		m,n = i,i
		for j in range(column_dimensions):

		#assiging subs to right side of the diagonal

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

		#assigning subs to left side of the diagonal

			if (j == n-1):
				arr[i,j] = sub_dict[entered_sub[4]]
			if (j == n-2):
				arr[i,j] = sub_dict[entered_sub[3]]
			if (j == n-3):
				arr[i,j] = sub_dict[entered_sub[2]]			
			if (j == n-4):
				arr[i,j] = sub_dict[entered_sub[1]]	
	return arr


def csv_converter(arr):
	
	with open(filename,"w") as object:
		for i in range(row_dimensions):
			arr_temp = arr[i]
			for j in range(column_dimensions):
				data = arr_temp[j]
				if j < (column_dimensions-1):
					data += ','
					
				object.write(data)
			object.write("\n")

	 
def dataframe_generator():
	df = pd.read_csv("database1.csv" , header = None)
	df.columns = headers
	
	return df

		














#calling the r_list_generator() function
entered_sub = r_list_generator(sub_dict_keys,entered_sub)


#calling the subject_assigner() function
arr = subject_assigner(sub_dict,entered_sub,arr)


#calling the csv_converter function
csv_converter(arr)


#calling the dataframe_generator function
df = dataframe_generator()


print(df)
