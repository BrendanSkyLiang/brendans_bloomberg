import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import numpy as numpy
from interface.data_sources.balance_sheet import annual_balance_sheet, quarterly_balance_sheet
from interface.data_sources.cashflow_statement import annual_cashflow, quarterly_cashflow
from interface.data_sources.income_statement import annual_income_statement, quarterly_income_statement
from interface.data_sources.price_history import price_history
from interface.data_sources.profile import profile

class Company():
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.profile = profile(symbol=self.symbol)
        self.price_history = price_history(self.symbol)
        self.annual_balance_sheet = annual_balance_sheet(symbol)
        self.quarterly_balance_sheet = quarterly_balance_sheet(symbol)
        self.annual_cashflow = annual_cashflow(symbol)
        self.quarterly_cashflow = quarterly_cashflow(symbol)
        self.annual_income_statement = annual_income_statement(symbol)
        self.quarterly_income_statement = quarterly_income_statement(symbol)












