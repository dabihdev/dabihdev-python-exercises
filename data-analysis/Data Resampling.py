import pandas as pd
import numpy as np

TIMERANGE_DAYS = 18

# Create a range of 15 days (DatetimeIndex)
dates = pd.date_range('2026-01-01', periods=TIMERANGE_DAYS, freq='D')

# Create a data series with that index
data = pd.Series(np.arange(TIMERANGE_DAYS), index=dates)

# Downsample to Weekly frequency ('W'), taking the mean
weekly_data = data.resample('W').mean()

print("Original Daily Data:")
print(data)
print("\nDownsampled Weekly Mean:")
print(weekly_data)