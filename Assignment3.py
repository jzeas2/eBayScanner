#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:21:43 2019
@co-author: Jonathan Zeas
@co-author: Kevin Ojeda

Assignment 3 - CS2300


"""

import sys

nn_docName = "sysmat2.txt"
onexn_docName = "prodvec2.txt"

nn_mx_file = open(nn_docName,"r")
onexn_mx_file = open(onexn_docName,"r")


print("\nSolving the System using Gaussian Elimination.\n\nLoading the vector info from file...\n\nSystem Matrix:\n")


for line in nn_mx_file:
    #Split the file by spaces
    array = line.split(" ")
    #reads first 2 numbers to decide how many values are in the matrix
    rows = int(array[0])
    col = int(array[0])
    #begins at second value
    arrayIndex = 1
    #initialize array with all 0s
    matrix_nn = [[0.0 for x in range(col+1)]for y in range (rows)]
    #for each column
    for i in range (0,col):
        #for each row
        for j in range (0,rows):
            #pick a value from text file and add to array
            #skip extra spaces
            while array[arrayIndex] == '':
                arrayIndex = arrayIndex + 1
            matrix_nn [i][j] = float(array[arrayIndex])
            arrayIndex+=1
nn_mx_file.close()

for line in onexn_mx_file:
    #Split the file by spaces
    array2 = line.split(" ")
    if array2[0] != '\n':
        #reads first 2 numbers to decide how many values are in the matrix
        rows2 = int(array2[0])
        col2 = 1
        if rows2 != rows:
            print("Rows are not equal in product vector & matrix.\n\n")
            sys.exit(1)
        #begins at second value
        arrayIndex = 1
        #for each row
        for i in range (0,rows2):
            #pick a value from text file and add to array
            #skip extra spaces
            while array2[arrayIndex] == '':
                arrayIndex = arrayIndex + 1
            matrix_nn [i][col] = float(array2[arrayIndex])
            arrayIndex+=1
onexn_mx_file.close()
#print the matrix
for row in matrix_nn:
    print(row)

#Shift highest ABS to top
high_val = 0
high_loc = 0

for k in range (0, rows):
    if abs(matrix_nn[k][0]) > abs(high_val):
        high_val = matrix_nn[k][0]
        high_loc = k

high_row = matrix_nn[high_loc]
matrix_nn[high_loc] = matrix_nn[0]
matrix_nn[0] = high_row


#start at column 0
on_col = 0
#for each column in the array
for i in range (0, int(array[0])):
    on_col+=1
    
    #for each row in the array that's greater than the column number
    for on_row in range (int(array[0]),i+1,-1):
        print("\nGoing for row,col - "+str(on_row)+","+str(on_col)+"\n")
        
        
        #get row to be zeroed
        row_tbz = matrix_nn[on_row-1]
        row_sub = matrix_nn[on_row-2]
        
        #zero the row
        new_row = [];
        #high row value over value to be zeroed
        scalar = row_sub[on_col-1]/row_tbz[on_col-1]
        #multiply each item by the scalar & append to new row
        for i in range (0,len(row_tbz)):
            row_tbz[i] = round(row_tbz[i] * scalar, 10)
            new_row.append(round(row_sub[i] - row_tbz[i],6))
        #push new row into the matrix
        matrix_nn[on_row-1] = new_row

        #print the matrix
        for row in matrix_nn:
            print(row)
            
            

#Calculate solution
sltn_mtrx = []
        
    
print('\nSolution Vector:')
#for each row starting at the bottom
for row in range(len(matrix_nn)-1,-1,-1):
    #calculate the known variable
    mult = matrix_nn[row][row]
    product = matrix_nn[row][rows]
    const = product/mult
    #add answer to solution matrix
    sltn_mtrx.append(const)
    #go through and calculate the new values in product vector based on the solution 
    for q in range (row-1,-1,-1):
        matrix_nn[q][rows2] = matrix_nn[q][rows2] - const * matrix_nn[q][row]
        
        
#print the solution vector
for i in range(len(sltn_mtrx)-1,-1,-1):
    print(round(sltn_mtrx[i],5))























