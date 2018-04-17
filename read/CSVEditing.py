import csv
import pandas as pd

def process_file(file_handle):
    df = pd.read_csv(file_handle)
    Predicted_Category = []
    # print(csvfile.columns)
    for index, row in df.iterrows():
        # print(row[4])
        Predicted_Category.append("Unknown")

    if 'Predicted_Category' not in df.columns:
        df.insert(loc=0, column='Predicted_Category', value=Predicted_Category)
    else:
        print('column name already exists')
        New_Column = pd.Series(Predicted_Category)
        df['Predicted_Category'] = New_Column.values

    return df

def download_file(file_handle):
    df = pd.read_csv(file_handle)
    Predicted_Category = []
    # print(csvfile.columns)
    for index, row in df.iterrows():
        # print(row[4])
        Predicted_Category.append("Unknown")

    if 'Predicted_Category' not in df.columns:
        df.insert(loc=0, column='Predicted_Category', value=Predicted_Category)
    else:
        print('column name already exists')
        New_Column = pd.Series(Predicted_Category)
        df['Predicted_Category'] = New_Column.values

    return df.to_csv(index=False)