import matplotlib.pyplot as plt
import numpy as np

import getdata

data = getdata.get_data('Dados\\glass.data')

means = []
std = []
median = []
skewness = []

rows = np.where(data[:,-1] == 7)

for column in data[rows].T:
	if column[0] == 0: continue
	#print(column)
	means.append(column[1:].mean())
	std.append(column[1:].std())
	median.append(np.median(column[1:]))

	v = sum([ (xi - means[-1])**2 for xi in column[1:] ])/len(column[1:] - 1)
	skewness_eq = sum([ (xi - means[-1])**3 for xi in column[1:] ])/(len(column[1:] - 1)*v**(3/2))
	skewness.append(skewness_eq)



show = data.T[2, 1:]
sub = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type']

# print(show)
# plt.stem(show)#, label=sub, align='left', histtype='barstacked', rwidth=700000)
# 	#range(len(show)), weights=
# plt.show()

fig, ax = plt.subplots(3, 5)
for n, column in enumerate(data[rows].T):
#	if column[0] == 0: continue
	show = column[1:]

	if column[0] == 5: print(show)

	axis = (n//5, n%5)

	ax[axis].set_title(sub[n])
	#ax[axis].hist(show)
	ax[axis].stem(show)#, histtype='barstacked')

ax[2, 1].set_title('means')
ax[2, 1].hist(range(len(means)), weights=means)

ax[2, 2].set_title('std')
ax[2, 2].hist(range(len(std)), weights=std)

ax[2, 3].set_title('median')
ax[2, 3].hist(range(len(median)), weights=median)

ax[2, 4].set_title('skewness')
ax[2, 4].hist(range(len(skewness)), weights=skewness)

plt.show()

'''Trabalhar com subplots'''