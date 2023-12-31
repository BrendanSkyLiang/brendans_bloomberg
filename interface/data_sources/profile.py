#!/usr/bin/env python3
import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg')
from interface.data_sources.api_key import api_key
import os
import pandas as pd

class profile():
    def __init__(self, symbol, path_root: str = r'/Users/brendanliang/Code/brendans_bloomberg') -> None:
        path = os.path.join(path_root, f'data/equities/{symbol}/profile.csv')
        profile = pd.read_csv(path)
        self.profile = profile.transpose()
        self.beta = float(self.profile.loc["beta"])
        self.avg_volume = int(self.profile.loc["volAvg"])
        self.name = self.profile.loc["companyName"]
        self.exchange = str(self.profile.loc["exchangeShortName"])
        self.industry = str(self.profile.loc["industry"])
        self.description = str(self.profile.loc["description"])
        self.sector = str(self.profile.loc["sector"])
        self.employees = int(self.profile.loc["fullTimeEmployees"])
        self.country = str(self.profile.loc["country"])