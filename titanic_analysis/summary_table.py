import pandas as pd

def create_summary_table(df):
    summary_data = {
        'Feature Name': df.columns,
        'Data Type': df.dtypes,
        'Number of Unique Values': [df[col].nunique() for col in df.columns],
        'Missing Values': [df[col].isnull().sum() for col in df.columns],
    }
    
    #summary dataframe
    summary_df = pd.DataFrame(summary_data)
    
    #handle missing values
    summary_df['Has Missing Values?'] = summary_df['Missing Values'].apply(lambda x: 'Yes' if x > 0 else 'No')
    summary_df.drop(columns='Missing Values', inplace=True)
    
    return summary_df

#test function execution and output
if __name__ == "__main__":
    filepath = "data/titanic.csv"  
    titanic_data = pd.read_csv(filepath)
    summary_table = create_summary_table(titanic_data)

    print(summary_table)  # Optional: to display the summary table
