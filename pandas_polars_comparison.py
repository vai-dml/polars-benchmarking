import polars as pl
import pandas as pd
from graph_plot import comparison_plot

import time


csv_file = '/Users/vaibhavkapur/Downloads/archive/Parking_Violations_Issued_-_Fiscal_Year_2017.csv'

# reading data with pandas-backed 
pd_start = time.time()
df_pd = pd.read_csv(csv_file)
pd_end = time.time()
pd_time = pd_end - pd_start

# reading data with pyarrow-backed nullable dtypes
pyarrow_start = time.time()
df_pd = pd.read_csv(csv_file,dtype_backend='pyarrow', engine='pyarrow')
pyarrow_end = time.time()
pyarrow_time = pyarrow_end - pyarrow_start

# reading data with polars - Lazyframe
pl_start = time.time()
df_pl = pl.scan_csv(csv_file,ignore_errors = True)
result_df = df_pl.collect()
pl_end = time.time()
pl_time = pl_end - pl_start

# plot
comparison_plot(pd_time, pyarrow_time, pl_time, "Comparion between Pandas and Polars execution time")







