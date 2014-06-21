'''
This contains simple plotting tools
'''

import pylab as plb
import numpy as np

def plot_in_line(myarray, figname='fig1.eps'):
	'''Expects a 2XN numpy array, and saves our figure.'''

	plb.plot(myarray[0],myarray[1],c='r',ls=':')
	plb.savefig(figname)

if __name__ == "__main__":
	'''Checks if we're just running plot_my_data.
	Run in the terminal as a script: python plot_in_line.py
	Open the figure in terminal: open fig1.eps'''

	myarray = np.array([range(30),[i**2 for i in range(30)]])
	plot_in_line(myarray) 
