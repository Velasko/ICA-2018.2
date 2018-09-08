import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import getdata

data = getdata.get_data('Dados\\glass.data')

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

# Calculating by glass type
means = []
std = []
median = []
skewness = []

for filter in range(1, 8):

	#because there is no data on the 4th type
	if filter == 4: 
		means.append([np.nan]*10)
		std.append([np.nan]*10)
		median.append([np.nan]*10)
		skewness.append([np.nan]*10)
		continue

	rows = np.where(data[:,-1] == filter)

	means.append([])
	std.append([])
	median.append([])
	skewness.append([])

	for n, column in enumerate(data[rows].T):
		if n == 0 : continue
		elif n != 1:
			column /= 100

		means[-1].append(column.mean())
		std[-1].append(column.std(dtype=np.float64))
		median[-1].append(np.median(column))

		try:
			skewness_eq = sum([ (xi - means[-1][-1])**3 for xi in column ])/((len(column) - 1)*std[-1][-1]**3)
			skewness[-1].append(skewness_eq)
		except ZeroDivisionError:
			skewness[-1].append(np.nan)


sub = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type'][1:]
labels = ["Tipo {}".format(e+1) for e in range(7)]
override = {'fontsize' : 'large', 'horizontalalignment' : 'center'}

fig, ax = plt.subplots(2, 2)
plt.setp(ax, xticks=range(len(sub)), xticklabels=sub)
bins = np.arange(len(sub)) - 0.5

# ax.ylabel('Concentração (%)')
plt.xlabel('Substâncias', override)

matrix = [[ e for e in range(len(means[0])) ]] * len(means)

ax[0, 0].set_title('Médias')
ax[0, 0].hist(matrix, weights=means, bins=bins)

ax[0, 1].set_title('Desvio Padrão')
ax[0, 1].hist(matrix, weights=std, bins=bins)

ax[1, 0].set_title('Medianas')
ax[1, 0].hist(matrix, weights=median, bins=bins)

ax[1, 1].set_title('Assimetria')
ax[1, 1].hist(matrix, weights=skewness, bins=bins)

plt.legend(labels)
plt.show()


# #plot de dados bruto
# fig, ax = plt.subplots(3, 5)
# for n, column in enumerate(data[rows].T):
# 	if n == 0: continue
# 	show = column

# 	if column[0] == 5: print(show)

# 	axis = (n//5, n%5)

# 	ax[axis].set_title(sub[n-1])
# 	#ax[axis].hist(show)
# 	ax[axis].stem(show)#, histtype='barstacked')

# plt.stem(show)#, label=sub, align='left', histtype='barstacked', rwidth=700000)
# 	#range(len(show)), weights=


#plt.show()