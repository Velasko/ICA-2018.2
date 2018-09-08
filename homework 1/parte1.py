import matplotlib.pyplot as plt
import numpy as np

import getdata

data = getdata.get_data('Dados\\glass.data')

means = []
std = []
median = []
skewness = []

general_std = [ column[1:].std() for column in data.T ]

for filter in range(1, 8):
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

		means[-1].append(column.mean())
		std[-1].append(column.std())
		median[-1].append(np.median(column))

		# try:
		# 	v = sum([ (xi - means[-1])**2 for xi in column ])/(len(column) - 1)
		# 	skewness_eq = sum([ (xi - means[-1])**3 for xi in column ])/((len(column) - 1)*v**(3/2))
		# 	skewness[-1].append(skewness_eq)
		# except ZeroDivisionError:
		# 	skewness[-1] = np.nan



sub = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type'][1:]


fig, ax = plt.subplots(2, 2)
plt.setp(ax, xticks=range(len(sub)), xticklabels=sub)
bins = np.arange(len(sub)) - 0.5

matrix = [[ e for e in range(len(means[0])) ]] * len(means)

ax[0, 0].set_title('means')
ax[0, 0].hist(matrix, weights=means, bins=bins)

ax[0, 1].set_title('std')
ax[0, 1].hist(matrix, weights=std, bins=bins)

ax[1, 0].set_title('median')
ax[1, 0].hist(matrix, weights=median, bins=bins)

ax[1, 1].set_title('skewness')
# ax[1, 1].hist(range(len(skewness[0])), weights=skewness)

# #plot de dados bruto
# for n, column in enumerate(data[rows].T):
# #	if column[0] == 0: continue
# 	show = column[1:]

# 	if column[0] == 5: print(show)

# 	axis = (n//5, n%5)

# 	ax[axis].set_title(sub[n])
# 	#ax[axis].hist(show)
# 	ax[axis].stem(show)#, histtype='barstacked')

# print(show)
# plt.stem(show)#, label=sub, align='left', histtype='barstacked', rwidth=700000)
# 	#range(len(show)), weights=


plt.show()