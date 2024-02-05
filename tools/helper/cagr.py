import numpy as np
from datetime import datetime

def cagr(dates, values):
    difference = abs(dates[0] - dates[-1])
    periods = difference[0].days / 365.25
    cagr = ((values[-1] / values[0]) ** (1 / periods)) - 1
    return cagr
    
    


