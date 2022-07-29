from operator import index
import numpy as np
import pandas as pd
import sys
import json
from datetime import datetime


def main(data_input_df, timeline, levels):
    ## transform logic
    # print(data_input_df.head())
    
    if timeline == "monthly":
        ## monthly logic
        print("monthly starts here \n")
        monthly(data_input_df, levels)
        # return (json.dumps(monthly(data_input_df), indent = 4))

    elif timeline == "yearly":
        ## yearly logic
        print("yearly starts here \n")
        yearly(data_input_df)
        # return (json.dumps(yearly(data_input_df), indent = 4))

def monthly(data_input_df, levels):
    
    report_view = []
    period_list = []
    dummy = []
    #print(data_input_df.columns[2])
    level_repository = list(np.zeros(levels))
    for i in range(levels):
        for j in data_input_df[data_input_df.columns[i+1]].unique(): #1+ because data has list order as 1st column
            dummy.append(j)
        level_repository[i] = dummy
        dummy = []
    print(level_repository)
    index_repository = []
    for level in range(levels):
        for level_name in level_repository[level]:
            dummy.append(data_input_df[data_input_df[data_input_df.columns[1+level]] == level_name].index.tolist()) #1+ because data has list order as first column
        index_repository.append(dummy)
        dummy = []
    print(index_repository)
    # for level in range(levels): #level = 0 points to level 1
    #     for level_name in level_repository[level]:
    #         level_index = level_repository[level].index(level_name)
    #         for month in data_input_df.columns[6:7]:   #remove 7 after 6 for all months later
    #             sum = 0
    #             # try :
    #             #     print(index_repository[level_index][level])
    #             # except :
    #             #     print(level_index, level)
    #             for j in (index_repository[level][level_index]):
    #                 sum = sum + data_input_df.iloc[j][month]
    #             print("{} {} sum is {}".format(level_name, month, sum))
    # Better way
    for level in range(0, levels):
        if level > 0: 
            for level_name in level_repository[level-1]: #level = 0 points to level 1
                previous_level_indexes = index_repository[level-1][level_repository[level-1].index(level_name)]
                for level_names_beyond_1 in level_repository[level]:
                    index = index_repository[level][level_repository[level].index(level_names_beyond_1)]
                    index_intersection = intersection(index, previous_level_indexes)
                    hierarchy = hierarchy_builder(level, level_repository, index_repository, index_intersection)
                    if(index_intersection != []):
                        for month in data_input_df.columns[6:16]: #2018 data 
                            sum = 0                   
                            for j in index_intersection:
                                sum = sum + data_input_df.iloc[j][month]                       
                            # hierarchy = str(isin(level_repository, index_repository, level-1, index_intersection)) + " -> " + str(level_names_beyond_1)
                            print("{} {} {}".format(hierarchy, month, sum))

        else :
            for level_name in level_repository[0]: #level = 0 points to level 1
                level_indexes = index_repository[0][level_repository[0].index(level_name)]  
                for month1 in data_input_df.columns[6:16]: #2018 data
                    sum = 0
                    for j in level_indexes:
                        sum = sum + data_input_df.iloc[j][month1]
                    print("{} {} sum is {}".format(level_name, month1, sum))      


def yearly(data_input_df):

    report_view = []

    # return dictionary

def intersection(lst1, lst2):

	temp = set(lst2)
	lst3 = [value for value in lst1 if value in temp]
	return lst3

def hierarchy_builder(level, level_repository, index_repository, index_intersection):
    hierarchy = ""
    for i in range(level+1):
        hierarchy = str(isin(level_repository, index_repository, level-i, index_intersection)) + " -> " + hierarchy
    return hierarchy


def isin(level_repository, index_repository, level, source_list):
    for j in index_repository[level]:
        if(set(source_list).issubset(set(j))):  
            return(level_repository[level][index_repository[level].index(j)])

if __name__ == '__main__' :
    path = sys.argv[1]
    timeline = sys.argv[2] #monthly or yearly
    levels = int(sys.argv[3])
    data_input = pd.read_excel(path, header = 0) #For header add no. of empty rows at top in dataset
    data_input_df = pd.DataFrame(data_input)
    column_names = list(data_input_df.columns[:6])
    for i in data_input_df.columns:
        if isinstance(i, datetime):
            column_names.append('{}-{}'.format(i.strftime("%m"), i.strftime("%Y")))
    data_input_df.columns = column_names
    main(data_input_df, timeline, levels)
