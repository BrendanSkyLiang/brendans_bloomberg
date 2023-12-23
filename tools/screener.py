import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg') 
import numpy as np
import pandas as pd
import os
import subprocess
import shlex
from interface.company import Company
from interface.forex import forex

path = "/Users/brendanliang/Code/brendans_bloomberg"
directories = subprocess.run(shlex.split(f"ls /Users/brendanliang/Code/brendans_bloomberg/data/equities"), capture_output=True, text=True)
list_directories = directories.stdout.splitlines()
