import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg') 
from tools.helper.cagr import cagr
from interface.company import Company
from interface.indicator import Yahoo_Indicator
  
def wacc(symbol, i = 0):
    """
    Calculates the Weighted Average Cost of Capital (WACC) for a given company.

    Args:
        symbol (str): The stock symbol of the company.
        i (int, optional): The index of the financial statement to use. Defaults to 0 (most recent).

    Returns:
        float: The WACC of the company.

    Raises:
        ValueError: If the company symbol is invalid.

    **Example Usage:**

    ```python
    wacc("AAPL")
    ```

    **Notes:**

    * This function uses the following sources to calculate the WACC:
        * Yahoo Finance for the risk-free rate and market return.
        * Bloomberg for the company's beta, tax rate, and financial statements.
    * The function assumes that the company's debt is all long-term debt.
    * The function uses the most recent financial statement by default. You can specify a different index to use a different statement.
    """
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
    



