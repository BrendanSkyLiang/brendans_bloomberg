import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
from interface.data_sources.api_key import api_key
import numpy as np
import pandas as pd
import fmpsdk

test = fmpsdk.cash_flow_statement(apikey=api_key, symbol="AAPL", period= "quarter")
fmpsdk.income_statement(apikey=api_key, symbol=)
# print(f"Company Profile: {fmpsdk.company_profile(apikey='3216c7fe0e242a23ecd409ba39236aa1', symbol=symbol)}")

# class company_balance_sheet():
    
    
print(test)
    
    