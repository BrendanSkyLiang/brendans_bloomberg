import sys
from torch import symbolize_tracebacks
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
from interface.data_sources.api_key import api_key
import os
from datetime import date
import pandas as pd
import yfinance as yf
import fmpsdk

def download_and_save_price_history(symbol, path_root:str = r'/Users/brendanliang/Code/brendans_bloomberg'):
    try:
        ph_raw = fmpsdk.historical_price_full(apikey=api_key, symbol=symbol,from_date="1950-01-01")
        ph = pd.DataFrame(ph_raw)
        date_list = []
        date_original = ph.loc[:,"date"]
        for i in range(len(date_original)):
            intermediate = date.fromisoformat(str(date_original[i]))
            date_list.append(intermediate)
        close = list(ph.loc[:,"close"])
        open = list(ph.loc[:,"open"])
        high = list(ph.loc[:,"high"])
        low = list(ph.loc[:,"low"])
        volume = list(ph.loc[:,"volume"])
        data = {"date": date_list, "open": open, "close": close, "volume": volume, "high": high, "low": low}
        combined = pd.DataFrame(data)
        combined.to_csv(f"{path_root}/data/equities/{symbol}/price_history.csv")
    except:
        try:
            tick = yf.Ticker(symbol)
            ph = pd.DataFrame(tick.history(period='max'))
            date_raw = ph.index
            date_list = []
            for i in range(len(date_raw)):
                intermediate = str(date_raw[i])
                datetime_intermediate = date.fromisoformat(intermediate[:10])
                date_list.append(datetime_intermediate)
            close = list(ph.loc[:,"Close"])
            open = list(ph.loc[:,"Open"])
            high = list(ph.loc[:,"High"])
            low = list(ph.loc[:,"Low"])
            volume = list(ph.loc[:,"Volume"])
            data = {"date": date_list, "open": open, "close": close, "volume": volume, "high": high, "low": low}
            combined = pd.DataFrame(data)
            combined.to_csv(f"{path_root}/data/equities/{symbol}/price_history.csv")
        except:
            try:
                pass
            except:
                raise RuntimeError("cannot attain price history")
        







