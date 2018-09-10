import matplotlib.pyplot as plt
import numpy as np

def get_data(filename):
	with open(filename, 'r') as file:
		f = file.readlines()

	x = np.array( [e for e in range(11) ] )#[['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type']])
	for line in f:
		l = line.split(",")

		new_line = [ float(data) for data in l ]
		x = np.vstack([x, new_line])

	return x


#Only afterwards I noticed I could've used pandas csv
data = get_data('Dados\\glass.data')

#Instanciating variables
sub = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type']
matrix = [e for e in range(len(data) -1 )]

means = []
std = []
median = []
skewness = []

fig, ax = plt.subplots(3, 5)
#	For each column in the data, in other words, for each
#category (named in the list sub)
for n, column in enumerate(data.T):
	#	In my script to get the datas from file, the first line is useless,
	#so I remove it with the folowing command
	column = column[1:]

	#deciding which subplot the current iteration will be drawn on
	axis = (n//5, n%5)

	#Identification of the current column and plotting
	ax[axis].set_title(sub[n])
	ax[axis].hist(column)

	#	Calculating current mean, median, standard deviation
	#and adding to vector to display the info from each col
	means.append(column.mean())
	median.append( np.median(column) )
	std.append( column.std() )

	#{3 sum from{i = 1} to{n} ( x_{i} - bar x )^{3} } over {( n - 1 ) times σ^{3} } 
	skewness_eq = sum([ (xi - means[n])**3 for xi in column[1:] ])/((len(column) - 2)*std[n]**(3))
	skewness.append(skewness_eq)

#discarting the ID's in the plot
sub = sub[1:]

#adding the categories in the subplots of the mean, median, standard deviation
for n in range(1, 5):
	plt.setp(ax[2, n], xticks=range(len(sub)), xticklabels=sub)

#the next 2 instanciations are for the situation where
#using bars is prefered.
#in such situation, must uncomment the  .hist lines
#and comment the .stem
bins = np.arange(len(sub)) - 0.5
matrix = [e for e in range(len(sub))]

ax[2, 1].set_title('Médias')
#ax[2, 1].hist(matrix, weights=means, bins=bins)
ax[2, 1].stem(means[1:])

ax[2, 2].set_title('Desvio Padrão')
#ax[2, 2].hist(matrix, weights=std, bins=bins)
ax[2, 2].stem(std[1:])

ax[2, 3].set_title('Medianas')
#ax[2, 3].hist(matrix, weights=median, bins=bins)
ax[2, 3].stem(median[1:])

ax[2, 4].set_title('Assimetria')
#ax[2, 4].hist(matrix, weights=skewness, bins=bins)
ax[2, 4].stem(skewness[1:])

plt.show()
