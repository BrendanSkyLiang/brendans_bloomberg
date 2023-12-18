#!/usr/bin/env python3
import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
from interface.data_sources.api_key import api_key
import os

import typing
import fmpsdk

print(api_key)

# # Company Valuation Methods
# symbol: str = "AAPL"
# print(f"Company Profile: {fmpsdk.company_profile(apikey='3216c7fe0e242a23ecd409ba39236aa1', symbol=symbol)}")