import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
from interface.data_sources.api_key import api_key
import os
from datetime import datetime
import pandas as pd
import numpy as np
import yfinance as yf
import fmpsdk

class price_history():
    def __init__(self, symbol:str, path_root:str = r'/Users/brendanliang/Code/brendans_bloomberg'):
        try:
            download_and_save_price_history(symbol=symbol)
        except: 
            print("price history not up to date, used saved file if avalible")
        if os.path.exists(os.path.join(path_root, f"data/equities/{symbol}/price_history.csv")):
            ph_raw = pd.read_csv(os.path.join(path_root, f"data/equities/{symbol}/price_history.csv"))
            self.price_history = ph_raw
            dates = self.price_history.loc[:,"date"]
            date_list = []
            for i in range(len(dates)):
                intermediate = datetime.fromisoformat(str(dates[i])).date()
                date_list.append(intermediate)
            self.dates = np.array(pd.DataFrame(date_list))
            self.close = np.array(self.price_history.loc[:,"close"])
            self.open = np.array(self.price_history.loc[:,"open"])
            self.high = np.array(self.price_history.loc[:,"high"])
            self.low = np.array(self.price_history.loc[:,"low"])
            self.volume = np.array(self.price_history.loc[:,"volume"])
        else:
            raise ValueError("price history cannot be obtained")

def download_and_save_price_history(symbol, path_root:str = r'/Users/brendanliang/Code/brendans_bloomberg'):
    # try:
    #     ph_raw = fmpsdk.historical_price_full(apikey=api_key, symbol=symbol,from_date="1950-01-01")
    #     ph = pd.DataFrame(ph_raw)
    #     date_list = []
    #     date_original = ph.loc[:,"date"]
    #     if len(date_original) < 10:
    #         exit()
    #     for i in range(len(date_original)):
    #         intermediate = date.fromisoformat(str(date_original[i]))
    #         date_list.append(intermediate)
    #     close = list(ph.loc[:,"close"])
    #     open = list(ph.loc[:,"open"])
    #     high = list(ph.loc[:,"high"])
    #     low = list(ph.loc[:,"low"])
    #     volume = list(ph.loc[:,"volume"])
    #     data = {"date": date_list, "open": open, "close": close, "volume": volume, "high": high, "low": low}
    #     combined = pd.DataFrame(data)
    #     combined.to_csv(f"{path_root}/data/equities/{symbol}/price_history.csv")
    # except:
    try:
        tick = yf.Ticker(symbol)
        ph = pd.DataFrame(tick.history(period='max'))
        date_raw = ph.index
        date_list = []
        if len(date_raw) < 10:
            exit()
        for i in range(len(date_raw)):
            intermediate = str(date_raw[i])
            datetime_intermediate = datetime.fromisoformat(intermediate[:10]).date()
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
        raise RuntimeError("cannot attain price history")

        







