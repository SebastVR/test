'''Assignment 1 - Introduction to Machine Learning
For this assignment, you will be using the Breast Cancer Wisconsin (Diagnostic) Database to create a 
classifier that can help diagnose patients. First, read through the description of the dataset (below).'''

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

'''The object returned by load_breast_cancer() is a scikit-learn Bunch object, which is similar to a 
dictionary.'''

print(cancer.keys())

'''Question 0 (Example)
How many features does the breast cancer dataset have?

This function should return an integer.'''

#---------- ANSWER CODE ----------
# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the number of features of the breast cancer dataset, which is an integer. 
    # The assignment question description will tell you the general format the autograder is expecting
    return len(cancer['feature_names'])

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 

#---------- ANSWER ----------
30

#-----------------------------------------------------------------------
'''Question 1
Scikit-learn works with lists, numpy arrays, scipy-sparse matrices, and pandas DataFrames, so converting the 
dataset to a DataFrame is not necessary for training this model. Using a DataFrame does however help make 
many things easier such as munging data, so let's practice creating a classifier with a pandas DataFrame.
Convert the sklearn.dataset cancer to a DataFrame.
This function should return a (569, 31) DataFrame with'''

columns =
    ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
    'mean smoothness', 'mean compactness', 'mean concavity',
    'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error',
    'smoothness error', 'compactness error', 'concavity error',
    'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area',
    'worst smoothness', 'worst compactness', 'worst concavity',
    'worst concave points', 'worst symmetry', 'worst fractal dimension',
    'target']
and index =
RangeIndex(start=0, stop=569, step=1)

#---------- ANSWER CODE ----------
def answer_one():
    df = pd.DataFrame(
            cancer['data'], 
            columns=cancer['feature_names']
    )
    df['target'] = cancer['target'].astype(float)
    return df

answer_one()

#---------- ANSWER ----------
'''     mean radius  mean texture  mean perimeter  mean area  ...  worst concave points  worst symmetry  worst fractal dimension  target
0          17.99         10.38          122.80     1001.0  ...                0.2654          0.4601                  0.11890     0.0
1          20.57         17.77          132.90     1326.0  ...                0.1860          0.2750                  0.08902     0.0
2          19.69         21.25          130.00     1203.0  ...                0.2430          0.3613                  0.08758     0.0
3          11.42         20.38           77.58      386.1  ...                0.2575          0.6638                  0.17300     0.0
4          20.29         14.34          135.10     1297.0  ...                0.1625          0.2364                  0.07678     0.0
..           ...           ...             ...        ...  ...                   ...             ...                      ...     ...
564        21.56         22.39          142.00     1479.0  ...                0.2216          0.2060                  0.07115     0.0
565        20.13         28.25          131.20     1261.0  ...                0.1628          0.2572                  0.06637     0.0
566        16.60         28.08          108.30      858.1  ...                0.1418          0.2218                  0.07820     0.0
567        20.60         29.33          140.10     1265.0  ...                0.2650          0.4087                  0.12400     0.0
568         7.76         24.54           47.92      181.0  ...                0.0000          0.2871                  0.07039     1.0

[569 rows x 31 columns]'''

#-----------------------------------------------------------------------
'''Question 2
What is the class distribution? (i.e. how many instances of malignant (encoded 0) and how many benign 
(encoded 1)?)
This function should return a Series named target of length 2 with integer values and 
index = ['malignant', 'benign']'''

#---------- ANSWER CODE ----------
def answer_two():
    cancerdf    = answer_one()
    serie       = cancerdf.groupby('target').count().iloc[:,0]
    serie.index = ['malignant', 'benign']
    serie.name  = 'target'
    return serie

answer_two()

#---------- ANSWER ----------
'''
malignant    212
benign       357
Name: target, dtype: int64'''

#-----------------------------------------------------------------------
'''Question 3
Split the DataFrame into X (the data) and y (the labels).
This function should return a tuple of length 2: (X, y), where

X, a pandas DataFrame, has shape (569, 30)
y, a pandas Series, has shape (569,).'''

#---------- ANSWER CODE ----------
def answer_three():
    cancerdf = answer_one()
    X = cancerdf[cancer['feature_names']]
    y = cancerdf['target']
    return X, y

answer_three()

#---------- ANSWER ----------
'''
(     mean radius  mean texture  mean perimeter  mean area  mean smoothness  ...  worst compactness  worst concavity  worst concave points  worst symmetry  worst fractal dimension
 0          17.99         10.38          122.80     1001.0          0.11840  ...            0.66560           0.7119                0.2654          0.4601                  0.11890
 1          20.57         17.77          132.90     1326.0          0.08474  ...            0.18660           0.2416                0.1860          0.2750                  0.08902
 2          19.69         21.25          130.00     1203.0          0.10960  ...            0.42450           0.4504                0.2430          0.3613                  0.08758
 3          11.42         20.38           77.58      386.1          0.14250  ...            0.86630           0.6869                0.2575          0.6638                  0.17300
 4          20.29         14.34          135.10     1297.0          0.10030  ...            0.20500           0.4000                0.1625          0.2364                  0.07678
 ..           ...           ...             ...        ...              ...  ...                ...              ...                   ...             ...                      ...
 564        21.56         22.39          142.00     1479.0          0.11100  ...            0.21130           0.4107                0.2216          0.2060                  0.07115
 565        20.13         28.25          131.20     1261.0          0.09780  ...            0.19220           0.3215                0.1628          0.2572                  0.06637
 566        16.60         28.08          108.30      858.1          0.08455  ...            0.30940           0.3403                0.1418          0.2218                  0.07820
 567        20.60         29.33          140.10     1265.0          0.11780  ...            0.86810           0.9387                0.2650          0.4087                  0.12400
 568         7.76         24.54           47.92      181.0          0.05263  ...            0.06444           0.0000                0.0000          0.2871                  0.07039

 [569 rows x 30 columns],
 0      0.0
 1      0.0
 2      0.0
 3      0.0
 4      0.0
       ... 
 564    0.0
 565    0.0
 566    0.0
 567    0.0
 568    1.0
 Name: target, Length: 569, dtype: float64)'''

#-----------------------------------------------------------------------
'''Question 4
Using train_test_split, split X and y into training and test sets (X_train, X_test, y_train, and y_test).
Set the random number generator state to 0 using random_state=0 to make sure your results match the 
autograder!
This function should return a tuple of length 4: (X_train, X_test, y_train, y_test), where

X_train has shape (426, 30)
X_test has shape (143, 30)
y_train has shape (426,)
y_test has shape (143,)'''

#---------- ANSWER CODE ----------
from sklearn.model_selection import train_test_split

def answer_four():
    X, y = answer_three()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
       
    return X_train, X_test, y_train, y_test

answer_four()

#---------- ANSWER ----------
'''
(     mean radius  mean texture  mean perimeter  mean area  ...  worst concavity  worst concave points  worst symmetry  worst fractal dimension
 293       11.850         17.46           75.54      432.7  ...          0.13160               0.09140          0.3101                  0.07007
 332       11.220         19.86           71.94      387.3  ...          0.01335               0.02022          0.3292                  0.06522
 565       20.130         28.25          131.20     1261.0  ...          0.32150               0.16280          0.2572                  0.06637
 278       13.590         17.84           86.24      572.3  ...          0.10600               0.05185          0.2335                  0.06263
 489       16.690         20.20          107.10      857.6  ...          0.24770               0.08737          0.4677                  0.07623
 ..           ...           ...             ...        ...  ...              ...                   ...             ...                      ...
 277       18.810         19.98          120.90     1102.0  ...          0.22100               0.12940          0.2567                  0.05737
 9         12.460         24.04           83.97      475.9  ...          1.10500               0.22100          0.4366                  0.20750
 359        9.436         18.32           59.82      278.6  ...          0.11440               0.05052          0.2454                  0.08136
 192        9.720         18.22           60.73      288.1  ...          0.00000               0.00000          0.1909                  0.06559
 559       11.510         23.93           74.52      403.5  ...          0.36300               0.09653          0.2112                  0.08732
 
 [426 rows x 30 columns],
      mean radius  mean texture  mean perimeter  mean area  ...  worst concavity  worst concave points  worst symmetry  worst fractal dimension
 512        13.40         20.52           88.64      556.7  ...          0.51060               0.20510          0.3585                  0.11090
 457        13.21         25.25           84.10      537.9  ...          0.13900               0.06005          0.2444                  0.06788
 439        14.02         15.66           89.59      606.5  ...          0.06260               0.08216          0.2136                  0.06710
 298        14.26         18.17           91.22      633.1  ...          0.15650               0.07530          0.2636                  0.07676
 37         13.03         18.42           82.61      523.8  ...          0.04833               0.05013          0.1987                  0.06169
 ..           ...           ...             ...        ...  ...              ...                   ...             ...                      ...
 236        23.21         26.97          153.50     1670.0  ...          0.58200               0.25930          0.3103                  0.08677
 113        10.51         20.19           68.64      334.2  ...          0.12950               0.06136          0.2383                  0.09026
 527        12.34         12.27           78.94      468.5  ...          0.17910               0.10700          0.3110                  0.07592
 76         13.53         10.94           87.91      559.2  ...          0.08539               0.07407          0.2710                  0.07191
 162        19.59         18.15          130.70     1214.0  ...          0.68100               0.22470          0.3643                  0.09223
 
 [143 rows x 30 columns],
 293    1.0
 332    1.0
 565    0.0
 278    1.0
 489    0.0
       ... 
 277    0.0
 9      0.0
 359    1.0
 192    1.0
 559    1.0
 Name: target, Length: 426, dtype: float64,
 512    0.0
 457    1.0
 439    1.0
 298    1.0
 37     1.0
       ... 
 236    0.0
 113    1.0
 527    1.0
 76     1.0
 162    0.0
 Name: target, Length: 143, dtype: float64)'''

#-----------------------------------------------------------------------
Question 5
'''Using KNeighborsClassifier, fit a k-nearest neighbors (knn) classifier with X_train, y_train and using one 
nearest neighbor (n_neighbors = 1).
This function should return a sklearn.neighbors.classification.KNeighborsClassifier'''

#---------- ANSWER CODE ----------
from sklearn.neighbors import KNeighborsClassifier

def answer_five():
    X_train, X_test, y_train, y_test = answer_four()
    knn = KNeighborsClassifier(n_neighbors = 1)
        
    return knn.fit(X_train, y_train)

answer_five()

#---------- ANSWER ----------
KNeighborsClassifier(n_neighbors=1)

#-----------------------------------------------------------------------
'''Question 6
Using your knn classifier, predict the class label using the mean value for each feature.
Hint: You can use cancerdf.mean()[:-1].values.reshape(1, -1) which gets the mean value for each feature, 
ignores the target column, and reshapes the data from 1 dimension to 2 (necessary for the precict method of 
KNeighborsClassifier).

This function should return a numpy array either array([ 0.]) or array([ 1.])'''

#---------- ANSWER CODE ----------
def answer_six():
    cancerdf = answer_one()
    means = cancerdf.mean()[:-1].values.reshape(1, -1)
    
    knn = answer_five()
    cancer_prediction = knn.predict( means )
        
    return cancer_prediction

answer_six()

#---------- ANSWER ----------
array([1.])

#-----------------------------------------------------------------------
'''Question 7
Using your knn classifier, predict the class labels for the test set X_test.
This function should return a numpy array with shape (143,) and values either 0.0 or 1.0.'''

#---------- ANSWER CODE ----------
def answer_seven():
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()

    return knn.predict(X_test)

answer_seven()

#---------- ANSWER ----------
'''
array([1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 0., 0., 1.,
       0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 1., 0., 1., 0., 1., 0.,
       1., 0., 1., 0., 1., 0., 0., 1., 0., 1., 0., 0., 1., 1., 1., 0., 0.,
       1., 0., 1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 0., 1., 0., 0.,
       0., 1., 1., 0., 1., 1., 0., 1., 1., 1., 1., 1., 0., 0., 0., 1., 0.,
       1., 1., 1., 0., 0., 1., 0., 1., 0., 1., 1., 0., 1., 1., 1., 1., 1.,
       1., 1., 0., 1., 0., 1., 0., 1., 1., 0., 0., 1., 1., 1., 0., 1., 1.,
       1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1.,
       1., 0., 0., 1., 1., 1., 0.])'''

#-----------------------------------------------------------------------
'''Question 8
Find the score (mean accuracy) of your knn classifier using X_test and y_test.
This function should return a float between 0 and 1'''

#---------- ANSWER CODE ----------
def answer_eight():
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()
    
    return knn.score(X_test, y_test)

answer_eight()

#---------- ANSWER ----------
0.916083916083916

#-----------------------------------------------------------------------
'''Optional plot
Try using the plotting function below to visualize the differet predicition scores between training and 
test sets, as well as malignant and benign cells'''

#---------- ANSWER CODE ----------
def accuracy_plot():
    import matplotlib.pyplot as plt

    #%matplotlib notebook

    X_train, X_test, y_train, y_test = answer_four()

    # Find the training and testing accuracies by target value (i.e. malignant, benign)
    mal_train_X = X_train[y_train==0]
    mal_train_y = y_train[y_train==0]
    ben_train_X = X_train[y_train==1]
    ben_train_y = y_train[y_train==1]

    mal_test_X = X_test[y_test==0]
    mal_test_y = y_test[y_test==0]
    ben_test_X = X_test[y_test==1]
    ben_test_y = y_test[y_test==1]

    knn = answer_five()

    scores = [knn.score(mal_train_X, mal_train_y), knn.score(ben_train_X, ben_train_y), 
                knn.score(mal_test_X, mal_test_y), knn.score(ben_test_X, ben_test_y)]


    plt.figure()

    # Plot the scores as a bar chart
    bars = plt.bar(np.arange(4), scores, color=['#4c72b0','#4c72b0','#55a868','#55a868'])

    # directly label the score onto the bars
    for bar in bars:
        height = bar.get_height()
        plt.gca().text(bar.get_x() + bar.get_width()/2, height*.90, '{0:.{1}f}'.format(height, 2), 
                        ha='center', color='w', fontsize=11)

    # remove all the ticks (both axes), and tick labels on the Y axis
    plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=True)

    # remove the frame of the chart
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.xticks([0,1,2,3], ['Malignant\nTraining', 'Benign\nTraining', 'Malignant\nTest', 'Benign\nTest'], alpha=0.8);
    plt.title('Training and Test Accuracies for Malignant and Benign Cells', alpha=0.8)
    plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/accuracy_plot.png')
accuracy_plot() 
#-----------------------------------------------------------------------