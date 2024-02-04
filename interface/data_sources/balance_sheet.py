import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import os
import numpy as np
import pandas as pd
import fmpsdk
from tools.helper.pandas_tools import find_col_index
from tools.helper.common_lists import find_common_set
from datetime import datetime

class annual_balance_sheet():
    def __init__(self, symbol, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/annual_balance_sheet.csv')
        balance_sheet = pd.read_csv(path)
        self.raw_balance_sheet = balance_sheet.transpose()
        self.balance_sheet: list = Balance_sheet(self.raw_balance_sheet).balance_list
        
class quarterly_balance_sheet():
    def __init__(self, symbol, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/quarterly_balance_sheet.csv')
        balance_sheet = pd.read_csv(path)
        self.raw_balance_sheet = balance_sheet.transpose()
        self.balance_sheet: list = Balance_sheet(self.raw_balance_sheet).balance_list

class Balance_sheet():
    def __init__(self, balance_sheet) -> None:
        balance_sheet_dict = {}
        for key in balance_sheet.index:
            if 'Unnamed' in key:
                pass
            else:
                balance_sheet_dict[key] = None
        self.balance_list = []
        for col_idx in balance_sheet:
            empty = balance_sheet_dict.copy()
            for key in balance_sheet_dict:
                if key == "fillingDate":
                    empty[key] = datetime.strptime(balance_sheet.loc[key,col_idx], "%Y-%m-%d").date()
                else:
                    empty[key] = balance_sheet.loc[key,col_idx]
            self.balance_list.append(empty)
