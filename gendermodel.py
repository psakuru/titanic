
import csv as csv
import numpy as np

train_file = csv.reader(open('./data/train.csv', 'rb'))
header = train_file.next()

data = []
for row in train_file:
    data.append(row)
data = np.array(data);


number_of_passengers = np.size(data[0::,1].astype(np.float));
number_of_survived = np.sum(data[0::,1].astype(np.float));

ratio_of_survival = number_of_survived/number_of_passengers;

print ratio_of_survival;

