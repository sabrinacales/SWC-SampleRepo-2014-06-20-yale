''' This module defines various methods to process data files.'''

import numpy as np

def readasnumpy(filename):
	'''This function takes in a tetfile, and returns a numpy array that 
	is the transpose of what is loaded.'''
	
	arr1 = np.loadtxt(filename)
	return arr1.T

def readlinebyline(filename):
	'''This function takes in a textile, and reads line by line.'''
	
	f = open(filename,'r')
	for line in f:
		print line
	f.close()

def printtonewtext(filename): 
	'''
	This function takes in a textfile, and prints the square of the 
	column to a new textfile.
	'''
	
	f = open(filename)
	fout = open('data3.txt','w')
	for line in f:
		# Use line.split() to split on whitespace
    		#print line
    		col1 = int(line.split(' ')[0])
    		#print col1
   		col2 = int(line.split(' ')[1])
    		#print col2
    		#print " "
    		#print " --- --- --- "   
    		# Get the sum of the first two columns
    		print >> fout, col2**2 # col1 col1+col2
	fout.close()
	f.close()


