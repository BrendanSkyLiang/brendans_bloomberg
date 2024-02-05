import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg') 
from tools.helper.cagr import cagr
from interface.company import Company
from interface.indicator import Yahoo_Indicator
  
def wacc(symbol, i = 0):
    tnx = Yahoo_Indicator("^TNX")
    risk_free_rate = tnx.close[-1]/100
    company = Company(symbol)
    # benchmark = Yahoo_Indicator("^SPX")
    # benchmark_cagr = cagr(benchmark.dates, benchmark.close)
    benchmark_cagr = 0.1067
    
    cost_of_equity = risk_free_rate + company.profile.beta * (benchmark_cagr - risk_free_rate)
    tax_rate = company.annual_income_statement.income_statement[0]["incomeTaxExpense"]/company.annual_income_statement.income_statement[0]["incomeBeforeTax"]
    total_equity = company.annual_balance_sheet.balance_sheet[0]["totalEquity"]
    total_debt = company.annual_balance_sheet.balance_sheet[0]["totalDebt"]
    cost_of_debt = company.annual_income_statement.income_statement[0]["interestExpense"]/total_debt

    # Calculate the weights of debt and equity
    equity_weight = total_equity / (total_equity + total_debt)  # Weight of equity
    debt_weight = 1 - equity_weight  # Weight of debt
    
    wacc = (cost_of_equity * equity_weight) + (cost_of_debt * (1 - tax_rate) * debt_weight)
    return wacc
    



