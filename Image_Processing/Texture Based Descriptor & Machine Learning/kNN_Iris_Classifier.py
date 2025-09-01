import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def getneighbour(Distance, y_train):
    count1 = 0
    count2 = 0
    print("Dis: ", Distance)
    for i in range(0, len(Distance)):
        A = y_train.iloc[Distance[i]]
        if A == 'Iris-setosa':
            count1 = count1 + 1
        else:
            count2 = count2 + 1
    print('count1', count1, 'count2', count2)
    if count1 > count2:
        return 'Iris-setosa'
    else:
        return 'Tris-versicolor'

def calculateminimumdistance(X_train, X_test, y_train, y_test, k):
    y_pred = [None] * len(y_test)
    for i in range(0, len(X_test)):
        dist = [0] * len(X_train)
        k1 = k
        for j in range(0, len(X_train)):
            testsl = X_test.iloc[i]['SepalLengthCm']
            testsw = X_test.iloc[i]['SepalWidthCm']
            testpl = X_test.iloc[i]['PetalLengthCm']
            testpw = X_test.iloc[i]['PetalWidthCm']
            trainsl = X_train.iloc[j]['SepalLengthCm']
            trainsw = X_train.iloc[j]['SepalWidthCm']
            trainpl = X_train.iloc[j]['PetalLengthCm']
            trainpw = X_train.iloc[j]['PetalWidthCm']
            value = distance.euclidean([testsl, testsw, testpl, testpw],
                                       [trainsl, trainsw, trainpl, trainpw])
            dist[j] = value

        min_dist_list_k = []
        while k1 > 0:
            minimumvalue = min(dist)
            nearestvalue = dist.index(minimumvalue)
            min_dist_list_k.append(nearestvalue)
            del dist[nearestvalue]  # Minimum distance ko remove kr rha h
            k1 = k1 - 1

        species = getneighbour(min_dist_list_k, y_train)
        print(species)
        y_pred[i] = species

    return y_pred

# Load and shuffle dataset
file = pd.read_csv("D:\Semester 6\DIP\Labs\Lab 12\Iris.csv")
file = file.sample(frac=1)

# Prepare features and labels
X = file.drop(['Species'], axis=1)
y = file['Species']

# User input for k
k = int(input("Enter Neighbour k: "))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Predict
y_pred = calculateminimumdistance(X_train, X_test, y_train, y_test, k)
print(y_pred)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
cm_df = pd.DataFrame(cm, index=['SETOSA','a','VERSICOLR'],
                     columns=['SETOSA','a','VERSICOLR'])

# Plotting the confusion matrix
plt.figure(figsize=(5,4))
sns.heatmap(cm_df, annot=True)
plt.title('Confusion Matrix')
plt.ylabel('Actual Values')
plt.xlabel('Predicted Values')
plt.show()
