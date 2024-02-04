import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg') 
from interface.company import Company


def trailing_twelve_month(symbol: str, financial_statement: str):
    if financial_statement == "balance_sheet":
        company = Company(symbol)
        statement = company.quarterly_balance_sheet.balance_sheet
        return statement
    elif financial_statement == "cashflow_statement":
        company = Company(symbol)
        statement = company.quarterly_cashflow.cashflow
    elif financial_statement == "income_statement":
        company = Company(symbol)
        statement = company.quarterly_income_statement.income_statement
    else:
        raise ValueError(f"financial statement {financial_statement} doesn't exist")
    statement = statement[::-1]
    ttm_statements = []
    raw_dict = {}
    
    for key, _ in statement[0].items():
        raw_dict[key] = None
    for i in range(3, len(statement)):
        empty = raw_dict.copy()
        for key, _ in statement[i].items():
            if type(statement[i][key]) == str or key == "calendarYear" or key == "fillingDate" or key == "cik" or key == "weightedAverageShsOutDil" or key == "weightedAverageShsOut" or "Ratio" in key:
                empty[key] = statement[i][key]
            else:
                empty[key] = statement[i][key] + statement[i-1][key] + statement[i-2][key] + statement[i-3][key]         
        ttm_statements.append(empty)
    ttm_statements = ttm_statements[::-1]
    return ttm_statements
    
trailing_twelve_month("GOOG", 'income_statement')













