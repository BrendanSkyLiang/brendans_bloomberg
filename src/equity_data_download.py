import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
from interface.data_sources.api_key import api_key
import pandas as pd
import fmpsdk
import os

def download_equity_data(symbol):
    if not os.path.exists(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}"):
        # Create the directory if it doesn't exist
        os.makedirs(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}")

    # Income Statements
    profile = fmpsdk.company_profile(apikey=api_key, symbol=symbol)
    profile = pd.DataFrame(profile)
    profile.transpose()
    profile.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/profile.csv",)

    # Income Statements
    quarterly_income_statement = fmpsdk.income_statement(apikey=api_key, symbol=symbol, period= "quarter",limit=100)
    q_income_statement = pd.DataFrame(quarterly_income_statement)
    q_income_statement.transpose()
    q_income_statement.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/quarterly_income_statement.csv")
    
    annual_income_statement = fmpsdk.income_statement(apikey=api_key, symbol=symbol, period= "annual",limit=100)
    a_income_statement = pd.DataFrame(annual_income_statement)
    a_income_statement.transpose()
    a_income_statement.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/annual_income_statement.csv")
    
    # Balance Sheets
    quarterly_balance_sheet = fmpsdk.balance_sheet_statement(apikey=api_key, symbol=symbol, period= "quarter",limit=100)
    q_balance_sheet = pd.DataFrame(quarterly_balance_sheet)
    q_balance_sheet.transpose()
    q_balance_sheet.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/quarterly_balance_sheet.csv")
    
    annual_balance_sheet = fmpsdk.balance_sheet_statement(apikey=api_key, symbol=symbol, period= "annual",limit=100)
    a_balance_sheet = pd.DataFrame(annual_balance_sheet)
    a_balance_sheet.transpose()
    a_balance_sheet.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/annual_balance_sheet.csv")
    
    # Cash Flow Statement
    quarterly_cashflow = fmpsdk.cash_flow_statement(apikey=api_key, symbol=symbol, period= "quarter",limit=100)
    q_cashflow = pd.DataFrame(quarterly_cashflow)
    q_cashflow.transpose()
    q_cashflow.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/quarterly_cashflow.csv")
    
    annual_cashflow = fmpsdk.cash_flow_statement(apikey=api_key, symbol=symbol, period= "annual",limit=100)
    a_cashflow = pd.DataFrame(annual_cashflow)
    a_cashflow.transpose()
    a_cashflow.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/annual_cashflow.csv")

    # Financial Ratios
    quarterly_financial_ratios = fmpsdk.financial_ratios(apikey=api_key, symbol=symbol, period= "quarter",limit=100)
    q_financial_ratios = pd.DataFrame(quarterly_financial_ratios)
    q_financial_ratios.transpose()
    q_financial_ratios.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/quarterly_financial_ratios.csv")
    
    annual_financial_ratios = fmpsdk.financial_ratios(apikey=api_key, symbol=symbol, period= "annual",limit=100)
    a_financial_ratios = pd.DataFrame(annual_financial_ratios)
    a_financial_ratios.transpose()
    a_financial_ratios.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/annual_financial_ratios.csv")

    # Key Metrics
    quarterly_key_metrics = fmpsdk.key_metrics(apikey=api_key, symbol=symbol, period= "quarter",limit=100)
    q_key_metrics = pd.DataFrame(quarterly_key_metrics)
    q_key_metrics.transpose()
    q_key_metrics.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/quarterly_key_metrics.csv")
    
    annual_key_metrics = fmpsdk.key_metrics(apikey=api_key, symbol=symbol, period= "annual",limit=100)
    a_key_metrics = pd.DataFrame(annual_key_metrics)
    a_key_metrics.transpose()
    a_key_metrics.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/annual_key_metrics.csv")

    # Dividends
    dividends = fmpsdk.historical_stock_dividend(apikey=api_key, symbol=symbol)
    conv1 = pd.DataFrame(dividends)
    conv2 = conv1.historical
    data_list = []
    for data in conv2:
        data_list.append(data)
    dividends = pd.DataFrame(data_list)
    dividends.transpose()
    dividends.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/dividends.csv")

    print(f"{symbol} has been updated")

# download_equity_data("AAPL")



