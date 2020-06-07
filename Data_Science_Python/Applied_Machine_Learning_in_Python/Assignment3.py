'''Assignment 3 - Evaluation
In this assignment you will train several models and evaluate how effectively they predict instances of 
fraud using data based on this dataset from Kaggle.
Each row in fraud_data.csv corresponds to a credit card transaction. Features include confidential variables 
V1 through V28 as well as Amount which is the amount of the transaction.
The target is stored in the class column, where a value of 1 corresponds to an instance of fraud and 0 
corresponds to an instance of not fraud.'''

import numpy as np
import pandas as pd

'''Question 1
Import the data from fraud_data.csv. What percentage of the observations in the dataset are instances of 
fraud?
This function should return a float between 0 and 1.'''

#---------- ANSWER CODE ----------
def answer_one():
    
    df = pd.read_csv('fraud_data.csv')
        
    return df.Class[df.Class==1].count()/df.Class.count()

answer_one()

#---------- ANSWER ----------
0.016410823768035772

#-----------------------------------------------------------------------
# Use X_train, X_test, y_train, y_test for all of the following questions
from sklearn.model_selection import train_test_split

df = pd.read_csv('fraud_data.csv')

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#-----------------------------------------------------------------------
'''Question 2
Using X_train, X_test, y_train, and y_test (as defined above), train a dummy classifier that classifies 
everything as the majority class of the training data. What is the accuracy of this classifier? What is the 
recall?
This function should a return a tuple with two floats, i.e. (accuracy score, recall score).'''

#---------- ANSWER CODE ----------
def answer_two():
    from sklearn.dummy import DummyClassifier
    from sklearn.metrics import recall_score
    
    dummy_majority = DummyClassifier(strategy = 'most_frequent').fit(X_train, y_train)
    accuracy = dummy_majority.score(X_test, y_test)
    y_dummy_predictions = dummy_majority.predict(X_test)
    recall = recall_score(y_test, y_dummy_predictions)
    
    return accuracy, recall

answer_two()

#---------- ANSWER ----------
(0.9852507374631269, 0.0)

#-----------------------------------------------------------------------
'''Question 3
Using X_train, X_test, y_train, y_test (as defined above), train a SVC classifer using the default 
parameters. What is the accuracy, recall, and precision of this classifier?
This function should a return a tuple with three floats, i.e. (accuracy score, recall score, precision 
score).'''

#---------- ANSWER CODE ----------
def answer_three():
    from sklearn.metrics import recall_score, precision_score
    from sklearn.svm import SVC
    
    svm = SVC().fit(X_train, y_train)
    svm_predicted = svm.predict(X_test)
    accuracy = svm.score(X_test, y_test)
    recall = recall_score(y_test, svm_predicted)
    precision = precision_score(y_test, svm_predicted)
    
    return (accuracy, recall, precision)

answer_three()

#---------- ANSWER ----------
(0.9900442477876106, 0.35, 0.9333333333333333)

#-----------------------------------------------------------------------
'''Question 4
Using the SVC classifier with parameters {'C': 1e9, 'gamma': 1e-07}, what is the confusion matrix when 
using a threshold of -220 on the decision function. Use X_test and y_test.
This function should return a confusion matrix, a 2x2 numpy array with 4 integers.'''

#---------- ANSWER CODE ----------
def answer_four():
    from sklearn.metrics import confusion_matrix,precision_recall_curve
    from sklearn.svm import SVC
    
    svm = SVC(C= 1e9, gamma= 1e-07).fit(X_train, y_train)
    #svm_predicted = svm.predict(X_test)
    #confusion_two = confusion_matrix(y_test, svm_predicted)
    
    y_scores = svm.decision_function(X_test)
    #precision, recall, thresholds = precision_recall_curve(y_test, y_scores)
    df = pd.DataFrame({'True Label':y_test,'Classifier score':y_scores}
                     ).sort_values(by='Classifier score').reset_index(drop=True)
    threshold_index = np.argmin(np.abs(df['Classifier score'] + 220))
    negative = df[:threshold_index+1]['True Label']
    positive = df[threshold_index+1:]['True Label']
    
    confusion = np.empty((2,2))
    
    confusion[0,0] = negative[negative==0].count()
    confusion[1,0] = negative[negative==1].count()
    confusion[1,1] = positive[positive==1].count()
    confusion[0,1] = positive[positive==0].count()
    return confusion

answer_four()

#---------- ANSWER ----------
array([[5320.,   24.],
       [  14.,   66.]])

#-----------------------------------------------------------------------
'''Question 5
Train a logisitic regression classifier with default parameters using X_train and y_train.

For the logisitic regression classifier, create a precision recall curve and a roc curve using y_test and 
the probability estimates for X_test (probability it is fraud).
Looking at the precision recall curve, what is the recall when the precision is 0.75?
Looking at the roc curve, what is the true positive rate when the false positive rate is 0.16?
This function should return a tuple with two floats, i.e. (recall, true positive rate).'''

#---------- ANSWER CODE ----------
def answer_five():
    from sklearn.metrics import precision_recall_curve, roc_curve
    from sklearn.linear_model import LogisticRegression

    lr = LogisticRegression().fit(X_train, y_train)
    y_scores_lr = lr.decision_function(X_test)
    
    precision, recall, thresholds = precision_recall_curve(y_test, y_scores_lr)
    closest_75 = np.argmin(np.abs(precision-.75))
    closest_75_r = recall[closest_75]

    fpr_lr, tpr_lr, _ = roc_curve(y_test, y_scores_lr)
    closest_16 = np.argmin(np.abs(fpr_lr-.16))
    closest_16_r = tpr_lr[closest_16]
    
    return closest_75_r, closest_16_r

answer_five()

#---------- ANSWER ----------
(0.825, 0.925)

#-----------------------------------------------------------------------
'''Question 6
Perform a grid search over the parameters listed below for a Logisitic Regression classifier, using recall 
for scoring and the default 3-fold cross validation.
'penalty': ['l1', 'l2']
'C':[0.01, 0.1, 1, 10, 100]
From .cv_results_, create an array of the mean test scores of each parameter combination. i.e.

l1	l2
0.01	?	?
0.1	?	?
1	?	?
10	?	?
100	?	?

This function should return a 5 by 2 numpy array with 10 floats.

Note: do not return a DataFrame, just the values denoted by '?' above in a numpy array. You might need to 
reshape your raw result to meet the format we are looking for.'''

#---------- ANSWER CODE ----------
def answer_six():    
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
grid_values = {'C':[0.01, 0.1, 1, 10, 100],'penalty': ['l1', 'l2']}

grid_clf = GridSearchCV(clf, param_grid = grid_values, scoring='recall', cv=3 )
grid_clf.fit(X_train, y_train)
y_decision_fn_scores = grid_clf.decision_function(X_test) 
    
    #print('Grid best parameter (max. recall): ', grid_clf.best_params_)
    #print('Grid best score (recall): ', grid_clf.best_score_)
    
    return grid_clf.cv_results_['mean_test_score'].reshape(5,2)

answer_six()

#---------- ANSWER ----------
array([[       nan, 0.79347826],
       [       nan, 0.80434783],
       [       nan, 0.79347826],
       [       nan, 0.80072464],
       [       nan, 0.80797101]])

# Use the following function to help visualize results from the grid search
def GridSearch_Heatmap(scores):
    #%matplotlib notebook
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.figure()
    sns.heatmap(scores.reshape(5,2), xticklabels=['l1','l2'], yticklabels=[0.01, 0.1, 1, 10, 100])
    plt.yticks(rotation=0);
    #plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/GridSearch_Heatmap.png')
    
GridSearch_Heatmap(answer_six())
#-----------------------------------------------------------------------