import numpy as np
import pandas as pd
import sys


def main(data_input_df):
    ## transform logic
    print(data_input_df.head())


if __name__ == '__main__':
    path = sys.argv[1]
    print(path)
    data_load = pd.read_excel(path)
    data_load_df = pd.DataFrame(data_load)
    main(data_load_df)
