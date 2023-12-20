import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import os
import numpy as np
import pandas as pd
import fmpsdk
from tools.pandas_tools import find_col_index
from tools.common_lists import find_common_set

class annual_balance_sheet():
    def __init__(self, symbol, year: int, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/annual_balance_sheet.csv')
        balance_sheet = pd.read_csv(path)
        self.balance_sheet = balance_sheet.transpose()
        self.balance_sheet_filing = balance_sheet_filing(self.balance_sheet, year, type="annual")
        
class quarterly_balance_sheet():
    def __init__(self, symbol,  year: int, quarter: str, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/quarterly_balance_sheet.csv')
        balance_sheet = pd.read_csv(path)
        self.balance_sheet = balance_sheet.transpose()
        self.balance_sheet_filing = balance_sheet_filing(self.balance_sheet, year, quarter, type="quarter")
        
class balance_sheet_filing():
    def __init__(self, balance_sheet, year: int, quarter: str = "na", type: str = "annual") -> None:
        if type == "annual":
            index = find_col_index(df=balance_sheet, target_value=year, row_index="calendarYear")
        elif type == "quarterly":
            index1 = find_col_index(df=balance_sheet, target_value=year, row_index="calendarYear")
            index2 = find_col_index(df=balance_sheet, target_value=quarter, row_index="period")
            index = find_common_set(index1, index2)
            if len(index) != 1:
                raise ValueError("more than one matching index, check balance sheet")
        else:
            raise ValueError("type must be either 'annual' or 'quarterly'.")
        
        relevant_column = balance_sheet.iloc[:,index]
        if type == "quarterly":
            self.period = str(relevant_column.loc["period"])
        self.date = str(relevant_column.loc["date"])
        self.currency = str(relevant_column.loc["reportedCurrency"])
        self.calendar_year = int(relevant_column.loc["calendarYear"])
        self.cash_and_cash_equivalents = int(relevant_column.loc["cashAndCashEquivalents"])
        self.short_term_investments = int(relevant_column.loc["shortTermInvestments"])
        self.net_receivables = int(relevant_column.loc["netReceivables"])
        self.inventory = int(relevant_column.loc["inventory"])
        self.other_current_assets = int(relevant_column.loc["otherCurrentAssets"])
        self.total_current_assets = int(relevant_column.loc["totalCurrentAssets"])
        self.ppe = int(relevant_column.loc["propertyPlantEquipmentNet"])
        self.goodwill = int(relevant_column.loc["goodwill"])
        self.intangible_assets = int(relevant_column.loc["intangibleAssets"])
        self.long_term_investments = int(relevant_column.loc["longTermInvestments"])
        self.tax_assets = int(relevant_column.loc["taxAssets"])
        self.other_non_current_assets = int(relevant_column.loc["otherNonCurrentAssets"])
        self.total_non_current_assets = int(relevant_column.loc["totalNonCurrentAssets"])
        self.other_assets = int(relevant_column.loc["otherAssets"])
        self.total_assets = int(relevant_column.loc["totalAssets"])
        
        self.account_payables = int(relevant_column.loc["accountPayables"])
        self.short_term_debt = int(relevant_column.loc["shortTermDebt"])
        self.tax_payables = int(relevant_column.loc["taxPayables"])
        self.deferred_revenue = int(relevant_column.loc["deferredRevenue"])
        self.other_current_liabilities = int(relevant_column.loc["otherCurrentLiabilities"])
        self.total_current_liabilities = int(relevant_column.loc["totalCurrentLiabilities"])
        self.long_term_debt = int(relevant_column.loc["longTermDebt"])
        self.deferred_non_current_revenue = int(relevant_column.loc["deferredRevenueNonCurrent"])
        self.defered_tax_liabilies_non_current = int(relevant_column.loc["deferredTaxLiabilitiesNonCurrent"])
        self.other_non_current_liabilities = int(relevant_column.loc["otherNonCurrentLiabilities"])
        self.total_non_current_liabilities = int(relevant_column.loc["totalNonCurrentLiabilities"])
        self.other_liabilities = int(relevant_column.loc["otherLiabilities"])
        self.capital_lease_obligations = int(relevant_column.loc["capitalLeaseObligations"])
        self.total_liabilities = int(relevant_column.loc["totalLiabilities"])
        
        self.preferred_stock = int(relevant_column.loc["preferredStock"])
        self.common_stock = int(relevant_column.loc["commonStock"])
        self.retained_earnings = int(relevant_column.loc["retainedEarnings"])
        self.other_comprehensive_income = int(relevant_column.loc["accumulatedOtherComprehensiveIncomeLoss"])
        self.other_total_stockholders_equity = int(relevant_column.loc["othertotalStockholdersEquity"])
        self.total_stockholders_equity = int(relevant_column.loc["totalStockholdersEquity"])
        self.total_equity = int(relevant_column.loc["totalEquity"])
        self.total_liabilities_and_stockholder_equity = int(relevant_column.loc["totalLiabilitiesAndStockholdersEquity"])
        self.minority_interest = int(relevant_column.loc["minorityInterest"])
        self.total_liabilities_and_total_stockholder_equity = int(relevant_column.loc["totalLiabilitiesAndTotalEquity"])
        
        self.total_investments = int(relevant_column.loc["totalInvestments"])
        self.total_debt = int(relevant_column.loc["totalDebt"])
        self.net_debt = int(relevant_column.loc["netDebt"])