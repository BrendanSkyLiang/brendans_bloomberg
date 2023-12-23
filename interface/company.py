import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import numpy as numpy
from interface.data_sources.balance_sheet import annual_balance_sheet, balance_sheet_filing, quarterly_balance_sheet
from interface.data_sources.cashflow_statement import annual_cashflow, quarterly_cashflow, cashflow_filing
from interface.data_sources.income_statement import annual_income_statement, quarterly_income_statement, income_statement_filing
from interface.data_sources.price_history import price_history
from interface.data_sources.profile import profile

class Company():
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.profile = profile(symbol=self.symbol)
        
    def get_price_history(self) -> price_history:
        return price_history(self.symbol)
        
    def get_annual_balance_sheet(self, year: int) -> balance_sheet_filing:
        return annual_balance_sheet(self.symbol, year=year).balance_sheet_filing
    
    def get_quarterly_balance_sheet(self, year:int, quarter: str) -> balance_sheet_filing:
        return quarterly_balance_sheet(self.symbol, year=year, quarter=quarter).balance_sheet_filing
    
    def get_annual_cashflow(self, year:int) -> cashflow_filing: 
        return annual_cashflow(self.symbol, year=year).cashflow_filing
    
    def get_quarterly_cashflow(self, year:int, quarter:str)->cashflow_filing:
        return quarterly_cashflow(self.symbol, year=year, quarter=quarter).cashflow_filing

    def get_annual_income_statement(self, year: int) -> income_statement_filing:
        return annual_income_statement(self.symbol, year=year).income_statement_filing
    
    def get_quarterly_income_statement(self, year:int, quarter: str) -> income_statement_filing:
        return quarterly_income_statement(self.symbol, year=year, quarter=quarter).income_statement_filing












