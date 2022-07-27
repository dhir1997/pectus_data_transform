import numpy as np
import pandas as pd
import sys
import json
from datetime import datetime


def main(data_input_df, timeline):
    ## transform logic
    # print(data_input_df.head())
    
    if timeline == "monthly":
        ## monthly logic
        print("monthly starts here \n")
        monthly(data_input_df)
        # return (json.dumps(monthly(data_input_df), indent = 4))

    elif timeline == "yearly":
        ## yearly logic
        print("yearly starts here \n")
        yearly(data_input_df)
        # return (json.dumps(yearly(data_input_df), indent = 4))

def monthly(data_input_df):
    
    report_view = []
    period_list = []
    #print(data_input_df.columns[2])
    level_1 = []
    for i in data_input_df["Level 1"].unique():
        level_1.append(i)
    print(level_1)
    for l in data_input_df.columns[6:]:
        for i in level_1:
            index_list = data_input_df[data_input_df['Level 1'] == i].index.tolist()
            sum = 0
            for j in range(len(data_input_df)):
                sum = sum + data_input_df.iloc[j][l]
            print("{} level 1 sum is {}".format(l, sum))


def yearly(data_input_df):

    report_view = []

    # return dictionary
    

if __name__ == '__main__' :
    path = sys.argv[1]
    timeline = sys.argv[2] #monthly or yearly
    levels = sys.argv[3]
    data_input = pd.read_excel(path, header = 0) #For header add no. of empty rows at top in dataset
    data_input_df = pd.DataFrame(data_input)
    column_names = list(data_input_df.columns[:6])
    print(type(column_names))
    for i in data_input_df.columns:
        if isinstance(i, datetime):
            column_names.append('{}-{}'.format(i.strftime("%m"), i.strftime("%Y")))
    data_input_df.columns = column_names
    print(data_input_df.columns)
    main(data_input_df, timeline, levels)
