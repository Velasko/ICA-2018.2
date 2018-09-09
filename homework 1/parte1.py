import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import getdata

data = getdata.get_data('Dados\\glass.data')


#plot de dados bruto
sub = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type']
matrix = [e for e in range(len(data) -1 )]

means = []
std = []
median = []
skewness = []

fig, ax = plt.subplots(3, 5)
for n, column in enumerate(data.T):
	column = column[1:]

	axis = (n//5, n%5)

	ax[axis].set_title(sub[n])
	# ax[axis].hist(matrix, weights=column[1:])
	ax[axis].hist(column)

	means.append(column.mean())
	median.append( np.median(column) )
	std.append( column.std() )

	skewness_eq = sum([ (xi - means[n])**3 for xi in column[1:] ])/((len(column) - 2)*std[n]**(3))
	skewness.append(skewness_eq)


sub = sub[1:]
for n in range(1, 5):
	plt.setp(ax[2, n], xticks=range(len(sub)), xticklabels=sub)
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


#calculating for general
means = [ column[1:].mean() for column in data.T ]
median = [ np.median(column[1:]) for column in data.T ]
std = [ column[1:].std(dtype=np.float64) for column in data.T ]
skewness = []

for n, column in enumerate(data.T):
	if column[0] == 0:
		continue

	skewness_eq = sum([ (xi - means[n])**3 for xi in column[1:] ])/((len(column) - 2)*std[n]**(3))
	skewness.append(skewness_eq)

