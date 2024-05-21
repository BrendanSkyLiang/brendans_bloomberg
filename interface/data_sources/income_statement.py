import sys
from jinja2 import pass_environment

from pyparsing import col
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import os
import numpy as np
import pandas as pd
import fmpsdk
from tools.helper.pandas_tools import find_col_index
from tools.helper.common_lists import find_common_set
from datetime import datetime

class annual_income_statement():
    def __init__(self, symbol, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/annual_income_statement.csv')
        income_statement = pd.read_csv(path)
        self.raw_income_statement = income_statement.transpose()
        self.income_statement: list = Income_statement(self.raw_income_statement).income_list
        
class quarterly_income_statement():
    def __init__(self, symbol, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/quarter_income_statement.csv')
        income_statement = pd.read_csv(path)
        self.raw_income_statement = income_statement.transpose()
        self.income_statement: list = Income_statement(self.raw_income_statement).income_list

class Income_statement():
    def __init__(self, income_statment) -> None:
        income_statement_dict = {}
        for key in income_statment.index:
            if 'Unnamed' in key:
                pass
            else:
                income_statement_dict[key] = None
        self.income_list = []
        for col_idx in income_statment:
            empty = income_statement_dict.copy()
            for key in income_statement_dict:
                if key == "fillingDate":
                    empty[key] =  datetime.strptime(income_statment.loc[key,col_idx], "%Y-%m-%d").date()
                else:
                    empty[key] = income_statment.loc[key,col_idx]
            self.income_list.append(empty)
