"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

def split_data(df_train, test_size=0.3, random_state=9999):
    """"Splits data into train and test datasets"""
    
    # Create a dependent variable
    X = df_train.drop('Survived', axis=1)
    y = df_train['Survived']

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=9999, stratify=y
    )
    return X_train, X_test, y_train, y_test


def fit_model(X_train, X_test, y_train, y_test):
    """ Fits a Classifier model using a trainind dataset"""
    
    classifier = tree.DecisionTreeClassifier()
    classifier = classifier.fit(X_train,y_train)
    
    ## Predicts test set
    y_pred = classifier.predict(X_test)
    
    ## Reports score
    score =  accuracy_score(y_test, y_pred)
    print(score)
    
    return classifier