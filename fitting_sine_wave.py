"""
Tools for fitting a sine wave.
They are not very reliable though so don't use this for science.
Though you can if you figure out what fitting algorithm to use. 
"""

import numpy as np


def generate_data(amp, freq, noise_amp):
	"""
	Generates data x, y where

	y = amp * sin(freq * x) + noise_amp * randn()
	"""
	np.arange(0.,80.,0.1)
	y = amp * np.sin(freq*x)
	y+= noise_amp * np.random.randn(len(y))
	return x,y


def plot_data(x,y,amp,freq,filename):
	"""
	Plot the actual data point x,y along with 
	the fit curve amp*sin(freq*x)
	"""
	plb.plot(x,y, 'b', linestyle = ':')
	y_fit = amp* np.sin(freq*x)
	plb.plot(x,y_fit,'r')
	plb.savefig(filename) # check here!


def fit_data(x,y,fmin_method, init_guess = np.array=([0.,0.,])):
	"""
	Fits data x, y to a sin wave using the fit 
	method fmin_method. Returns the fitted 
	amplitude and frequency.

	This is usually unstable so you should usually
	""""
	def objective_func(A):
	return sum((y-A[0]*np.sin()) #not finished here
	fmin_method(objective_func, init_guess)
