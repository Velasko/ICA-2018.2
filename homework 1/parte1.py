import matplotlib.pyplot as plt
import numpy as np

import getdata

data = getdata.get_data('Dados\\glass.data')


# for column in data.T:
# 	if column[0] == 0:
# 		continue
# 	print(column[1:].mean())

means = [ column[1:].mean() for column in data.T ]
std = [ column[1:].std() for column in data.T ]
median = [ np.median(column[1:]) for column in data.T ]
skewness = [ 3*(means[x] - median[x])/std[x] for x, _ in enumerate(means) ]


show = median
sub = ['RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe']

print(show)
#plt.hist(range(len(show)), weights=show, label=sub, align='left', histtype='barstacked', rwidth=700000)

#print(help(plt.hist))

#plt.hist(np.ones((len(data), len(data[0]))), weights=data, label=sub)

# for column in data.T:
# 	show = column[1:]
# 	plt.hist(range(len(show)), weights=show, label=sub, align='left', histtype='barstacked', rwidth=700000)
# 	plt.show()

#print(data[3])