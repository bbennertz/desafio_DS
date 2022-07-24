"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.1
"""
import pandas as pd

def preprocess_train(df_train: pd.DataFrame):
    """ This function cleanses the titanic train raw data, removing cabines, names and transforming Sex in sex_female and sex_male, when true == 1 """
    
    #remove unused columns
    df_train = df_train.drop(columns=['Cabin','Name'])
    
    #remove null values
    df_train = df_train.dropna()
    
    #creating sex an unique value
    df_train = pd.get_dummies(df_train, columns=['Sex'])
    
    # Select numerical columns
    num_cols = ['PassengerId', 'Pclass', 'Age', 'SibSp', 'Parch', 'Sex_female', 'Sex_male', 'Fare']
    cols_to_select = num_cols + ['Survived']

    # Select only numerical columns
    df_train = df_train[cols_to_select]

    return df_train

def preprocess_test(df_test: pd.DataFrame):
    """ This function cleanses the titanic test raw data, removing cabines, names and transforming Sex in sex_female and sex_male, when true == 1 """
    
    #remove unused columns
    df_test = df_test.drop(columns=['Cabin','Name'])
    
    #remove null values
    df_test = df_test.dropna()
    
    #creating sex an unique value
    df_test = pd.get_dummies(df_test, columns=['Sex'])

    # Select numerical columns
    num_cols = ['PassengerId', 'Pclass', 'Age', 'SibSp', 'Parch', 'Sex_female', 'Sex_male', 'Fare']
    cols_to_select_test = num_cols

    # Select only numerical columns
    df_test = df_test[cols_to_select_test]

    return df_test