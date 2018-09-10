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


data = getdata.get_data('Dados\\glass.data')

# Calculating by glass type
means = []
std = []
median = []
skewness = []

sub = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type'][1:-1]
labels = ["Tipo {}".format(e+1) for e in range(7)]
override = {'fontsize' : 'large', 'horizontalalignment' : 'center'}

for filter in range(1, 8):

	#because there is no data on the 4th type
	if filter == 4:
		size = len(sub)
		means.append([np.nan]*size)
		std.append([np.nan]*size)
		median.append([np.nan]*size)
		skewness.append([np.nan]*size)
		continue

	rows = np.where(data[:,-1] == filter)

	means.append([])
	std.append([])
	median.append([])
	skewness.append([])

	fig, ax = plt.subplots(3, 5)
	for n, column in enumerate(data[rows].T):
		if n == 0 or n == 10 : continue
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

		#plotting raw data from current type
		n -= 1
		axis = (n//5, n%5)
		ax[axis].set_title(sub[n])
		ax[axis].hist(column)

	for n in range(4):
		plt.setp(ax[2, n], xticks=range(len(sub)), xticklabels=sub)

	ax[2, 0].set_title('Médias')
	ax[2, 0].stem(means[-1])

	ax[2, 1].set_title('Desvio Padrão')
	ax[2, 1].stem(std[-1])

	ax[2, 2].set_title('Medianas')
	ax[2, 2].stem(median[-1])

	ax[2, 3].set_title('Assimetria')
	ax[2, 3].stem(skewness[-1])

	plt.suptitle('Plots sobre o Tipo {}'.format(filter))
#	plt.show()

#sub = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'k', 'Ca', 'Ba', 'Fe', 'type'][1:-1]
fig, ax = plt.subplots(2, 2)
plt.setp(ax, xticks=range(len(sub)), xticklabels=sub)
bins = np.arange(len(sub)) - 0.5

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
plt.suptitle('Plots sobre todos os tipos')
plt.show()
