import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import os
import numpy as np
import pandas as pd
import fmpsdk
from tools.helper.pandas_tools import find_col_index
from tools.helper.common_lists import find_common_set

class annual_cashflow():
    def __init__(self, symbol, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/annual_cashflow.csv')
        cashflow = pd.read_csv(path)
        self.raw_cashflow = cashflow.transpose()
        self.cashflow: list = Cashflow(self.raw_cashflow).cashflow_list
        
class quarterly_cashflow():
    def __init__(self, symbol, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/quarterly_cashflow.csv')
        cashflow = pd.read_csv(path)
        self.raw_cashflow = cashflow.transpose()
        self.cashflow: list = Cashflow(self.raw_cashflow).cashflow_list

class Cashflow():
    def __init__(self, cashflow_statment) -> None:
        cashflow_dict = {}
        for key in cashflow_statment.index:
            if 'Unnamed' in key:
                pass
            else:
                cashflow_dict[key] = None
        self.cashflow_list = []
        for col_idx in cashflow_statment:
            empty = cashflow_dict.copy()
            for key in cashflow_dict:
                empty[key] = cashflow_statment.loc[key,col_idx]
            self.cashflow_list.append(empty)