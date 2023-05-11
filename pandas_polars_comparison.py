import polars as pl
import pandas as pd
from graph_plot import comparison_plot

import time


csv_file = '/Users/vaibhavkapur/Downloads/archive/Parking_Violations_Issued_-_Fiscal_Year_2017.csv'

# reading data with polars - Lazyframe
pl_start = time.time()
df_pl = pl.scan_csv(csv_file,ignore_errors = True)
result_df = df_pl.collect()
size = result_df.estimated_size()
pl_end = time.time()
pl_time = pl_end - pl_start

# reading data with pandas
pd_start = time.time()
df_pd = pd.read_csv(csv_file,on_bad_lines='skip')
pd_end = time.time()
pd_time = pd_end - pd_start

print(size)
# plot
comparison_plot(pd_time,pl_time, "Comparion between Pandas and Polars execution time")







