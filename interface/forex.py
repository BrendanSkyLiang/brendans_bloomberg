import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import numpy as np 
import pandas as pd 
import os
from tools.helper.pandas_tools import find_col_index

def forex(original_currency:str, new_currency:str, root:str = r'/Users/brendanliang/Code/brendans_bloomberg'):
    """
    Retrieves the exchange rate between two currencies.

    Args:
        original_currency: A string containing the original.
        new_currency: A string containing the new currency.

    Returns:
        The exchange rate as a float. So that ORIGINAL * output = New Currency
    """
    forex_table = pd.read_csv(os.path.join(root, "data/forex/forex_list.csv"))
    relevant_index = find_col_index(forex_table.transpose(), f"{original_currency}/{new_currency}", "name")
    return float(forex_table.loc[relevant_index, "price"])
    