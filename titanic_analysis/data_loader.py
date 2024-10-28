import pandas as pd

def get_numerical_df(df, numerical_features):
    #filtering dataFrame
    numerical_df = df[numerical_features].copy()
    return numerical_df

#test functions execution and output
if _name_ == "_main_":
    filepath = "data/titanic.csv" 
    titanic_data = pd.read_csv(filepath)
    numerical_features = ['Age', 'Fare']
    numerical_df = get_numerical_df(titanic_data, numerical_features)
