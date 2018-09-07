import numpy as np

class MyArray(np.ndarray):
	def get_title(self, index):
		return ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type'][index]

def get_data(filename):
	with open(filename, 'r') as file:
		f = file.readlines()

	x = np.array( [e for e in range(11) ] )#[['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type']])
	for line in f:
		l = line.split(",")

		new_line = [ float(data) for data in l ]
		x = np.vstack([x, new_line])

	return x



