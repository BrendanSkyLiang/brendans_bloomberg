import sys
from turtle import down
from datetime import datetime, timedelta
import os
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import numpy as numpy
from interface.data_sources.balance_sheet import annual_balance_sheet, quarterly_balance_sheet
from interface.data_sources.cashflow_statement import annual_cashflow, quarterly_cashflow
from interface.data_sources.income_statement import annual_income_statement, quarterly_income_statement
from interface.data_sources.price_history import PriceHistory
from interface.data_sources.profile import profile
from src.equity_data_download import download_equity_data

class Company():
    def __init__(self, symbol) -> None:
        """
        This class represents a company and provides access to its financial data.

        Args:
            symbol (str): The stock symbol of the company.

        Raises:
            ValueError: If the company symbol is invalid.

        **Example Usage:**

        ```python
        company = Company("AAPL")
        print(company.profile.name)  # Print the company name
        print(company.annual_income_statement.income_statement[0]["revenue"])  # Print the company's revenue for the most recent year
        ```
        **Notes:**

        * This class uses the following sources to retrieve financial data:
            * Yahoo Finance for price history.
            * Financial Modeling Prep (FMP) for all other financial data.
        * The financial data is downloaded and cached locally.
        * The data is updated automatically if it is older than 72 hours.
        """
        # Check when the data was last updated
        data_path = f"/Users/brendanliang/Code/brendans_bloomberg/data/equities/{symbol}/quarter_balance_sheet.csv"

        # Get the last modified time of the data directory
        last_updated = datetime.fromtimestamp(os.path.getmtime(data_path))

        # Update data if it's older than 24 hours
        update_interval = timedelta(hours=72)
        if datetime.now() - last_updated > update_interval:
            try:
                download_equity_data(symbol)
            except:
                print("Error downloading data, using cached data")        
                
        self.symbol = symbol
        self.profile = profile(symbol=self.symbol)
        self.price_history = PriceHistory(self.symbol)
        self.annual_balance_sheet = annual_balance_sheet(symbol)
        self.quarterly_balance_sheet = quarterly_balance_sheet(symbol)
        self.annual_cashflow = annual_cashflow(symbol)
        self.quarterly_cashflow = quarterly_cashflow(symbol)
        self.annual_income_statement = annual_income_statement(symbol)
        self.quarterly_income_statement = quarterly_income_statement(symbol)












