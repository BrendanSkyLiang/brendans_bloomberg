import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
import os
import numpy as np
import pandas as pd
import fmpsdk
from tools.find_col_index import find_col_index
from tools.common_lists import find_common_set

class annual_income_statement():
    def __init__(self, symbol, year: int, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/annual_income_statement.csv')
        income_statement = pd.read_csv(path)
        self.income_statement = income_statement.transpose()
        self.income_statement = income_statement_filing(self.income_statement, year, type="annual")
        
class quarterly_income_statement():
    def __init__(self, symbol,  year: int, quarter: str, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/quarterly_income_statement.csv')
        income_statement = pd.read_csv(path)
        self.income_statement = income_statement.transpose()
        self.income_statement_filing = income_statement_filing(self.income_statement, year, quarter, type="quarter")
        
class income_statement_filing():
    def __init__(self, income_statement, year: int, quarter: str = "na", type: str = "annual") -> None:
        if type == "annual":
            index = find_col_index(df=income_statement, target_value=year, row_index="calendarYear")
        elif type == "quarterly":
            index1 = find_col_index(df=income_statement, target_value=year, row_index="calendarYear")
            index2 = find_col_index(df=income_statement, target_value=quarter, row_index="period")
            index = find_common_set(index1, index2)
            if len(index) != 1:
                raise ValueError("more than one matching index, check income_statement statment")
        else:
            raise ValueError("type must be either 'annual' or 'quarterly'.")
        
        relevant_column = income_statement.iloc[:,index]
        self.period = str(relevant_column.loc["period"])
        self.date = str(relevant_column.loc["date"])
        self.currency = str(relevant_column.loc["reportedCurrency"])
        self.calendar_year = int(relevant_column.loc["calendarYear"])
        
        self.revenue = int(relevant_column.loc["revenue"])
        self.cogs = int(relevant_column.loc["costOfRevenue"])
        self.gross_profit = int(relevant_column.loc["grossProfit"])
        self.gross_profit_ratio = int(relevant_column.loc["grossProfitRatio"])
        self.research_and_development = int(relevant_column.loc["researchAndDevelopmentExpenses"])
        self.general_and_admin_expenses = int(relevant_column.loc["generalAndAdministrativeExpenses"])
        self.selling_and_marketing_expenses = int(relevant_column.loc["sellingAndMarketingExpenses"])
        self.selling_general_and_admin_expenses = int(relevant_column.loc["sellingGeneralAndAdministrativeExpenses"])
        self.other_expenses = int(relevant_column.loc["otherExpenses"])
        self.operating_expenses = int(relevant_column.loc["operatingExpenses"])
        self.cost_and_expenses = int(relevant_column.loc["costAndExpenses"])
        self.interest_income = int(relevant_column.loc["interestIncome"])
        self.interest_expense = int(relevant_column.loc["interestExpense"])
        self.depreciation_and_amortization = int(relevant_column.loc["depreciationAndAmortization"])
        self.ebitda = int(relevant_column.loc["ebitda"])
        self.ebitda_ratio = int(relevant_column.loc["ebitdaratio"])
        self.operating_income = int(relevant_column.loc["operatingIncome"])
        self.operating_income_ratio = int(relevant_column.loc["operatingIncomeRatio"])
        self.total_other_income_or_expenses = int(relevant_column.loc["totalOtherIncomeExpensesNet"])
        self.income_before_tax = int(relevant_column.loc["incomeBeforeTax"])
        self.income_before_tax_ratio = int(relevant_column.loc["incomeBeforeTaxRatio"])
        self.income_tax_expense = int(relevant_column.loc["incomeTaxExpense"])
        self.net_income = int(relevant_column.loc["netIncome"])
        self.net_income_ratio = int(relevant_column.loc["netIncomeRatio"])
        self.eps = int(relevant_column.loc["eps"])
        self.eps_diluted = int(relevant_column.loc["epsdiluted"])
        self.weighted_average_shs_out = int(relevant_column.loc["weightedAverageShsOut"])
        self.weighted_average_shs_out_diluted = int(relevant_column.loc["weightedAverageShsOutDil"])