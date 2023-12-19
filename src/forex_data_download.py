import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
from interface.data_sources.api_key import api_key
import pandas as pd
import fmpsdk
import os

def download_forex_data():
    forex_list = fmpsdk.forex_list(apikey=api_key)
    forex_list = pd.DataFrame(forex_list)
    forex_list.to_csv(f"/Users/brendanliang/Code/brendans_bloomberg/data/forex/forex_list.csv")











