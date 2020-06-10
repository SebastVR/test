'''Assignment 4 - Understanding and Predicting Property Maintenance Fines
This assignment is based on a data challenge from the Michigan Data Science Team (MDST).
The Michigan Data Science Team (MDST) and the Michigan Student Symposium for Interdisciplinary Statistical 
Sciences (MSSISS) have partnered with the City of Detroit to help solve one of the most pressing problems 
facing Detroit - blight. Blight violations are issued by the city to individuals who allow their properties 
to remain in a deteriorated condition. Every year, the city of Detroit issues millions of dollars in fines 
to residents and every year, many of these fines remain unpaid. Enforcing unpaid blight fines is a costly 
and tedious process, so the city wants to know: how can we increase blight ticket compliance?
The first step in answering this question is understanding when and why a resident might fail to comply 
with a blight ticket. This is where predictive modeling comes in. For this assignment, your task is to 
predict whether a given blight ticket will be paid on time.
All data for this assignment has been provided to us through the Detroit Open Data Portal. Only the data 
already included in your Coursera directory can be used for training the model for this assignment. 
Nonetheless, we encourage you to look into data from other Detroit datasets to help inform feature creation 
and model selection. We recommend taking a look at the following related datasets:

Building Permits
Trades Permits
Improve Detroit: Submitted Issues
DPD: Citizen Complaints
Parcel Map
We provide you with two data files for use in training and validating your models: train.csv and test.csv. 
Each row in these two files corresponds to a single blight ticket, and includes information about when, why, 
and to whom each ticket was issued. The target variable is compliance, which is True if the ticket was paid 
early, on time, or within one month of the hearing data, False if the ticket was paid after the hearing date or not at all, and Null if the violator was found not responsible. Compliance, as well as a handful of other variables that will not be available at test-time, are only included in train.csv.

Note: All tickets where the violators were found not responsible are not considered during evaluation. 
They are included in the training set as an additional source of data for visualization, and to enable 
unsupervised and semi-supervised approaches. However, they are not included in the test set.

File descriptions (Use only this data for training your model!)

readonly/train.csv - the training set (all tickets issued 2004-2011)
readonly/test.csv - the test set (all tickets issued 2012-2016)
readonly/addresses.csv & readonly/latlons.csv - mapping from ticket id to addresses, and from addresses to 
lat/lon coordinates. 
Note: misspelled addresses may be incorrectly geolocated.

Data fields

train.csv & test.csv

ticket_id - unique identifier for tickets
agency_name - Agency that issued the ticket
inspector_name - Name of inspector that issued the ticket
violator_name - Name of the person/organization that the ticket was issued to
violation_street_number, violation_street_name, violation_zip_code - Address where the violation occurred
mailing_address_str_number, mailing_address_str_name, city, state, zip_code, non_us_str_code, country - Mailing address of the violator
ticket_issued_date - Date and time the ticket was issued
hearing_date - Date and time the violator's hearing was scheduled
violation_code, violation_description - Type of violation
disposition - Judgment and judgement type
fine_amount - Violation fine amount, excluding fees
admin_fee - $20 fee assigned to responsible judgments
state_fee - $10 fee assigned to responsible judgments
late_fee - 10% fee assigned to responsible judgments
discount_amount - discount applied, if any
clean_up_cost - DPW clean-up or graffiti removal cost
judgment_amount - Sum of all fines and fees
grafitti_status - Flag for graffiti violations
train.csv only

payment_amount - Amount paid, if any
payment_date - Date payment was made, if it was received
payment_status - Current payment status as of Feb 1 2017
balance_due - Fines and fees still owed
collection_status - Flag for payments in collections
compliance [target variable for prediction] 
 Null = Not responsible
 0 = Responsible, non-compliant
 1 = Responsible, compliant
compliance_detail - More information on why each ticket was marked compliant or non-compliant
Evaluation
Your predictions will be given as the probability that the corresponding blight ticket will be paid on time.
The evaluation metric for this assignment is the Area Under the ROC Curve (AUC).
Your grade will be based on the AUC score computed for your classifier. A model which with an AUROC of 0.7 
passes this assignment, over 0.75 will recieve full points.
For this assignment, create a function that trains a model to predict blight ticket compliance in Detroit 
using readonly/train.csv. Using this model, return a series of length 61001 with the data being the 
probability that each corresponding ticket from readonly/test.csv will be paid, and the index being the 
ticket_id.

Example:

ticket_id
   284932    0.531842
   285362    0.401958
   285361    0.105928
   285338    0.018572
             ...
   376499    0.208567
   376500    0.818759
   369851    0.018528
   Name: compliance, dtype: float32
Hints
Make sure your code is working before submitting it to the autograder.

Print out your result to see whether there is anything weird (e.g., all probabilities are the same).
Generally the total runtime should be less than 10 mins. You should NOT use Neural Network related 
classifiers (e.g., MLPClassifier) in this question.
Try to avoid global variables. If you have other functions besides blight_model, you should move those 
functions inside the scope of blight_model.
Refer to the pinned threads in Week 4's discussion forum when there is something you could not figure it 
out.'''

#---------- ANSWER CODE ----------
import pandas as pd
import numpy as np

def blight_model():

    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from sklearn.model_selection import train_test_split,GridSearchCV
    from sklearn.metrics import roc_auc_score

    train = pd.read_csv('train.csv',encoding='latin1',engine='python')
    train.set_index('ticket_id',inplace=True)

    test = pd.read_csv('test.csv')
    test.set_index('ticket_id',inplace=True)

    #Cleaning Data
    train = train[train.compliance.notnull()]
    train = train.loc[train.city.str.lower() == 'detroit']
    y_train = train.compliance
    train = train.loc[:,train.columns.isin(test.columns)]

    drop_columns = [
        'admin_fee','state_fee','late_fee','clean_up_cost',
        'mailing_address_str_number','mailing_address_str_name',
        'grafitti_status','non_us_str_code', 'inspector_name',
        'violation_zip_code','violation_street_name','violation_description',
        'violation_code','violation_street_number','violator_name',
        'country','city','zip_code','state',
        'ticket_issued_date', 'hearing_date',
    ]
    train.drop(drop_columns, axis=1, inplace=True)
    test.drop(drop_columns, axis=1, inplace=True)

    X_train = pd.get_dummies(train)
    X_test = pd.get_dummies(test)

    X_test = X_test.loc[:,X_test.columns.isin(X_train.columns)]
    X_train = X_train.loc[:,X_train.columns.isin(X_test.columns)]

    #Set Classifiers

    #GBC
    gbc = GradientBoostingClassifier().fit(X_train, y_train)
    #print ('Accuracy GBC: ',gbc.score(X_train,y_train))

    y_decision_fn_scores_auc_gbc = gbc.decision_function(X_test) 

    y_predict = gbc.predict_proba(X_test)
    ###
    #print('Test set AUC: ', roc_auc_score(y_train, y_decision_fn_scores_auc_gbc[:,0]))

    #grid_gbc = {'learning_rate':[0.01, 0.1, 1, 10] , 'max_depth':[2, 3, 4, 5]}

    #grid_gbc_auc = GridSearchCV(gbc, param_grid = grid_gbc, scoring = 'roc_auc')
    #grid_gbc_auc.fit(X_train, y_train)
    #y_decision_fn_scores_auc_gbc = grid_gbc_auc.decision_function(X_test) 

    #print('Grid best parameter (max. AUC): ', grid_gbc_auc.best_params_)
    #print('Grid best score (AUC): ', grid_gbc_auc.best_score_)

    #RFC
    #rfc = RandomForestClassifier().fit(X_train, y_train)
    #print ('Accuracy GBC: ',rfc.score(X_train,y_train))
    #y_predict = rfc.predict_proba(X_test)
    #grid_rfc = {'max_features':[8,10] , 'max_depth':[2, 3, 4, 5]}

    #grid_rfc_auc = GridSearchCV(rfc, param_grid = grid_rfc, scoring = 'roc_auc')
    #grid_rfc_auc.fit(X_train, y_train)
    #y_decision_fn_scores_auc = grid_rfc_auc.decision_function(X_test) 

    #print('Grid best parameter (max. AUC): ', grid_rfc_auc.best_params_)
    #print('Grid best score (AUC): ', grid_rfc_auc.best_score_)

    return pd.Series(y_predict[:,1],index=X_test.index,name='compliance')

blight_model()

#---------- ANSWER ----------
'''
ticket_id
284932    0.045475
285362    0.009447
285361    0.054110
285338    0.045475
285346    0.054110
            ...   
376496    0.009275
376497    0.009275
376499    0.047782
376500    0.047782
369851    0.413674
Name: compliance, Length: 61001, dtype: float64'''
#-----------------------------------------------------------------------