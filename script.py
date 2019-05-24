import datapackage
import pandas as pd
import time


def get_dataset():
    data_url = 'https://datahub.io/machine-learning/iris/datapackage.json'
    package = datapackage.Package(data_url)
    resources = package.resources

    for resource in resources:
        if resource.tabular:
            data = pd.read_csv(resource.descriptor['path'])
            return data

def compute_class(petal_length):
    if petal_length <= 2:
        return 1
    elif 2 < petal_length <5:
        return 2
    else:
        return 3

data = get_dataset()

# For-loop method
start = time.time()

class_list = []
for i in range(len(data)):
    petal_length = data.iloc[i]['petallength']
    class_num = compute_class(petal_length)
    class_list.append(class_num)
end = time.time()
print("For-loop run time = {}".format(end-start))

# Looping with .iterrows(), similar to enumerate()
start1 = time.time()
class_list1 = []
for idx, data_row in data.iterrows():
    petal_length = data_row['petallength']
    class_num = compute_class(petal_length)
    class_list1.append(class_num)
end1 = time.time()
print("Iterrows run time =  {}".format(end1-start1))

# Without loops .apply()
start2 = time.time()
class_list2 = data.apply(lambda row: compute_class(row['petallength']), axis=1) 
    # axis 0 or index: apply function to each column, 1 or columns: apply function to each row
end2 = time.time()
print(".apply() run time =  {}".format(end2-start2))

# With .cut()
start3 = time.time()
class_list3 = pd.cut(x=data.petallength,
                        bins=[0,2,5,100], # range
                        include_lowest=True, # include_lowest: Whether the first interval should be left-inclusive or not. ???
                        labels = [1, 2, 3]).astype(int) # labels = return value
end3 = time.time()
print(".cut() run time =  {}".format(end3-start3))




