import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
from interface.data_sources.api_key import api_key
import pandas as pd
import fmpsdk
import os

def download_equity_data(symbol):
    """Downloads equity data for a given company symbol.

    Args:
        symbol (str): The stock symbol of the company.

    Returns:
        None

    Raises:
        ValueError: If the company symbol is invalid.

    **Example Usage:**

    ```python
    download_equity_data("AAPL")
    ```

    **Notes:**

    * This function uses the Financial Modeling Prep (FMP) API to download equity data.
    * The function downloads the following data for the company:
        * Profile
        * Income Statements (quarterly and annual)
        * Balance Sheets (quarterly and annual)
        * Cash Flow Statements (quarterly and annual)
        * Financial Ratios (quarterly and annual)
        * Key Metrics (quarterly and annual)
        * Dividends
    * The data is saved to the following directory:
        `/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}`
    * The function creates the directory if it doesn't exist.
    """
    
    # Create the directory if it doesn't exist
    os.makedirs(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}", exist_ok=True)
    
    # Income Statements
    profile = fmpsdk.company_profile(apikey=api_key, symbol=symbol)
    profile = pd.DataFrame(profile)
    profile.transpose()
    profile.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/profile.csv",)
    
    api_calls = {
        "income_statement": fmpsdk.income_statement,
        "balance_sheet": fmpsdk.balance_sheet_statement,
        "cash_flow_statement": fmpsdk.cash_flow_statement,
        "financial_ratios": fmpsdk.financial_ratios,
        "key_metrics": fmpsdk.key_metrics,
    }

    for statement, api_call in api_calls.items():
        for period in ["quarter", "annual"]:
            data = api_call(apikey=api_key, symbol=symbol, period=period, limit=100)
            df = pd.DataFrame(data)
            df.transpose()
            df.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/{period}_{statement}.csv")

    print(f"{symbol} has been updated")

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





