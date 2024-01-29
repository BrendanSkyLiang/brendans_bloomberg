import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg') 
import numpy as np
import pandas as pd
import os
import subprocess
import shlex
import datetime
from interface.company import Company
from interface.data_sources.balance_sheet import annual_balance_sheet, quarterly_balance_sheet
from interface.data_sources.cashflow_statement import annual_cashflow, quarterly_cashflow
from interface.data_sources.income_statement import annual_income_statement, quarterly_income_statement
import math


def trailing_twelve_month(symbol: str, financial_statement: str, yr = 2021):
    if financial_statement == "balance_sheet":
        statement = quarterly_balance_sheet(symbol, yr, "Q4").balance_sheet
    elif financial_statement == "cashflow_statement":
        statement = quarterly_cashflow(symbol, yr, "Q4").cashflow
    elif financial_statement == "income_statement":
        statement = quarterly_income_statement(symbol, yr, "Q4").income_statement
    else:
        raise ValueError(f"financial statement {financial_statement} doesn't exist")
    
    df = statement
    
    ttm_df = pd.DataFrame(columns=df.)  # Create an empty dataframe for TTM data

    for i in range(len(df)):
        if i >= 4:  # Only calculate TTMs for quarters where data is available
            prev_year_qtr = i - 4

            # Calculate TTM values for numeric columns
            ttm_df.loc[df.index[i], df.select_dtypes(include=[np.number]).columns] = df.iloc[i:prev_year_qtr:-1].sum(axis=0) + df.iloc[i, df.select_dtypes(include=[np.number]).columns]

            # Fill string columns with original values
            ttm_df.loc[df.index[i], df.select_dtypes(exclude=[np.number]).columns] = df.iloc[i, df.select_dtypes(exclude=[np.number]).columns]

    print(ttm_df)


print(trailing_twelve_month("GOOG", "cashflow_statement"))
    














