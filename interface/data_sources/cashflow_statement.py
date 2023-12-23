import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import os
import numpy as np
import pandas as pd
import fmpsdk
from tools.helper.pandas_tools import find_col_index
from tools.helper.common_lists import find_common_set

class annual_cashflow():
    def __init__(self, symbol, year: int, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/annual_cashflow.csv')
        cashflow = pd.read_csv(path)
        self.cashflow = cashflow.transpose()
        self.cashflow = cashflow_filing(self.cashflow, year, type="annual")
        
class quarterly_cashflow():
    def __init__(self, symbol,  year: int, quarter: str, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/quarterly_cashflow.csv')
        cashflow = pd.read_csv(path)
        self.cashflow = cashflow.transpose()
        self.cashflow_filing = cashflow_filing(self.cashflow, year, quarter, type="quarter")
        
class cashflow_filing():
    def __init__(self, cashflow, year: int, quarter: str = "na", type: str = "annual") -> None:
        if type == "annual":
            index = find_col_index(df=cashflow, target_value=year, row_index="calendarYear")
        elif type == "quarterly":
            index1 = find_col_index(df=cashflow, target_value=year, row_index="calendarYear")
            index2 = find_col_index(df=cashflow, target_value=quarter, row_index="period")
            index = find_common_set(index1, index2)
            if len(index) != 1:
                raise ValueError("more than one matching index, check cashflow statment")
        else:
            raise ValueError("type must be either 'annual' or 'quarterly'.")
        
        relevant_column = cashflow.iloc[:,index]
        self.period = str(relevant_column.loc["period"])
        self.date = str(relevant_column.loc["date"])
        self.currency = str(relevant_column.loc["reportedCurrency"])
        self.calendar_year = int(relevant_column.loc["calendarYear"])
        self.net_income = int(relevant_column.loc["netIncome"])
        self.depreciation_and_amortization = int(relevant_column.loc["depreciationAndAmortization"])
        self.deferred_income_tax = int(relevant_column.loc["deferredIncomeTax"])
        self.stock_based_compensation = int(relevant_column.loc["stockBasedCompensation"])
        self.change_in_working_capital = int(relevant_column.loc["changeInWorkingCapital"])
        self.accounts_recievables = int(relevant_column.loc["accountsReceivables"])
        self.inventory = int(relevant_column.loc["inventory"])
        self.accounts_payables = int(relevant_column.loc["accountsPayables"])
        self.other_working_capital = int(relevant_column.loc["otherWorkingCapital"])
        self.other_non_cash_items = int(relevant_column.loc["otherNonCashItems"])
        self.cash_from_operating_activities = int(relevant_column.loc["netCashProvidedByOperatingActivities"])
        self.ppe_investment = int(relevant_column.loc["investmentsInPropertyPlantAndEquipment"])
        self.net_acquisitions = int(relevant_column.loc["acquisitionsNet"])
        self.purches_of_investments = int(relevant_column.loc["purchasesOfInvestments"])
        self.sales_maturities_of_investments = int(relevant_column.loc["salesMaturitiesOfInvestments"])
        self.other_investing_activities = int(relevant_column.loc["otherInvestingActivites"])
        self.cash_used_for_investing_activities = int(relevant_column.loc["netCashUsedForInvestingActivites"])
        self.debt_repayment = int(relevant_column.loc["debtRepayment"])
        self.common_stock_issued = int(relevant_column.loc["commonStockIssued"])
        self.common_stock_repurchased = int(relevant_column.loc["commonStockRepurchased"])
        self.dividends_paid = int(relevant_column.loc["dividendsPaid"])
        self.other_financing_activities = int(relevant_column.loc["otherFinancingActivites"])
        self.financing_cashflow = int(relevant_column.loc["netCashUsedProvidedByFinancingActivities"])
        self.effect_of_forex = int(relevant_column.loc["effectOfForexChangesOnCash"])
        self.net_change_in_cash = int(relevant_column.loc["netChangeInCash"])
        self.cash_at_end = int(relevant_column.loc["cashAtEndOfPeriod"])
        self.cash_at_beginning = int(relevant_column.loc["cashAtBeginningOfPeriod"])
        self.operating_cashflow = int(relevant_column.loc["operatingCashFlow"])
        self.capex = int(relevant_column.loc["capitalExpenditure"])     
        self.free_cash_flow = int(relevant_column.loc["freeCashFlow"])