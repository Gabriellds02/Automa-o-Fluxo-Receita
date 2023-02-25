from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
import time
from datetime import date
from dataclasses import replace
from http.client import ImproperConnectionState
import os
from time import time
import pandas as pd
import glob
from pathlib import Path
import pathlib
import time



joined_files = os.path.join("/home", "mydata*.csv")
joined_list = glob.glob(joined_files)
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)


#df = pd.concat(
    #map(pd.read_csv, ['1', '2']), ignore_index=True)
#print(df)







