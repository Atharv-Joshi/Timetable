#importing required packages
import numpy as np
import random as rd
import pandas as pd
import streamlit as st


#declaring the required variables
column_dimensions = 5
row_dimensions = 5
filename = 'database1.csv'

#declaring required arrays
entered_sub = []
arr = np.zeros((row_dimensions,column_dimensions))
arr = arr.astype(np.object)
headers = ['8:50-9:50','9:50-10:50','10:50-11:50','11:50-12:50','12:50-1:50']

#declaring dictionary containing the subject names
sub_dict = {1 : 'pps', 2 : 'phy', 3 : 'bee', 4 : 'sme', 5: 'M1'}
sub_dict_keys = list(sub_dict.keys())
sub_dict_values = list(sub_dict.values())


#dictionary  containing teacher names
teachers = {'pps':['A','a'],'phy':['B','b'],"bee":['C','c'],'sme':['D','d'],'M1':['E','e']}



#function which randomizes the keys in the subject dicitionary
def r_list_generator(sub_dict_values,entered_sub):
	while(len(entered_sub) <= 4):
		temp = rd.choice(sub_dict_values)
		if temp not in entered_sub:
			entered_sub.append(temp)
	return(entered_sub)

		



#assigning the subjects to the array cells
def subject_assigner(entered_sub,arr):

	for i in range(row_dimensions):
		m,n = i,i
		for j in range(column_dimensions):

		#assiging subs to right side of the diagonal

			if ( j == n):
				arr[i,j] = entered_sub[0]

			elif (j == n+1):
				arr[i,j] = entered_sub[1]
			elif (j == n+2):
				arr[i,j] = entered_sub[2]	
			elif (j == n+3):
				arr[i,j] = entered_sub[3]
			elif (j == n+4):
				arr[i,j] = entered_sub[4]		

		#assigning subs to left side of the diagonal

			elif (j == n-1):
				arr[i,j] = entered_sub[4]
			elif (j == n-2):
				arr[i,j] = entered_sub[3]
			elif (j == n-3):
				arr[i,j] = entered_sub[2]			
			elif (j == n-4):
				arr[i,j] = entered_sub[1]	
	return arr


#converts the database which is of array type into a .csv type file
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


#generates a dataframe using the .csv type file 
def dataframe_generator():
	df = pd.read_csv("database1.csv" , header = None)
	df.columns = headers

	
	return df
		














#calling the r_list_generator() function
entered_sub = r_list_generator(sub_dict_values,entered_sub)


#calling the subject_assigner() function
arr = subject_assigner(entered_sub,arr)


#calling the csv_converter function
csv_converter(arr)


#calling the dataframe_generator function
df = dataframe_generator()


st.write(df)
