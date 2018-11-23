import time

start = time.time()

import _pickle as picles
from sklearn.metrics import confusion_matrix
from sklearn import linear_model

def get_data(filename):
	return picles.Unpickler(open('grantData_hw3/' + filename + '.pickle', 'rb')).load()

train = get_data('training')
testing = get_data('testing')
reduced_set = get_data('reduced')

#Training:
x = train[reduced_set['x']]
y = train['Class']

classifier = linear_model.LogisticRegression(solver='liblinear')
classifier.fit(x, y)

#Testing:
test_x = testing[reduced_set['x']]
test_y = testing['Class']

predic_y = classifier.predict(test_x)

assertion = [test_y[n] == item for n, item in enumerate(predic_y)]

print('Logistic Regression:')

corrects = assertion.count(True)
wrongs = assertion.count(False)

matrix = confusion_matrix(test_y, predic_y)
print(matrix)

print(corrects/(corrects+wrongs))

print('Execution time:', time.time()-start)