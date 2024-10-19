import yfinance as yf
import numpy as np
import pandas as pd
from datetime import time, datetime, timedelta

ticker = "EURUSD=X"
interval = "1m"


# Define start and end dates for the data
end_date = datetime.today().date()
start_date = end_date - timedelta(days=20)

# Define start and end times for the data

start_time = time(hour=9, minute=30)
end_time = time(hour=16, minute=0)

# Initialize an empty DataFrame to store the data

data = pd.DataFrame()

# Loop over the 4 batches of data
for i in range(4):

  # Define the period for this batch of data

  period_end = end_date - timedelta(days=i * 5)
  period_start = period_end - timedelta(days=5)
  period = f"{period_start:%Y-%m-%d} {period_end:%Y-%m-%d}"

  # Download historical data from Yahoo Finance

  batch_data = yf.download(ticker, start=period_start, end=period_end, interval=interval)

  # Convert index to DatetimeIndex if necessary
  batch_data = batch_data.set_index(pd.DatetimeIndex(batch_data.index))

  # Filter data between start_time and end_time
  batch_data = batch_data.between_time(start_time, end_time)

  # Append the batch data to the overall data DataFrame
  data = pd.concat([data, batch_data])

  # Filter overall data between start_time and end_time
  data = data.between_time(start_time, end_time)

  n = 5

  dn_fractals = (data['High'].shift(2) < data['High']) & (data['High'].shift(1) < data['High']) & (data['High'].shift(-1) < data['High']) & (data['High'].shift(-2) < data['High'])
  up_fractals = (data['Low'].shift(2) > data['Low']) & (data['Low'].shift(1) > data['Low']) & (data['Low'].shift(-1) > data['Low']) & (data['Low'].shift(-2) > data['Low'])

  # Plot fractals
  data.loc[dn_fractals, 'fractal'] = data.loc[dn_fractals, 'Low']
  data.loc[up_fractals, 'fractal'] = data.loc[up_fractals, 'High']
  data['fractal'].fillna(method='ffill', inplace=True)
  data['fractal'].fillna(method='bfill', inplace=True)

  # Calculate Mode and Standard Deviations (Modified)

# Up Fractals
up_fractal_rotations = data['High'] - data['fractal']
up_fractal_rotations = up_fractal_rotations[up_fractal_rotations != 0]
up_mode = np.mean(up_fractal_rotations)  # Use mean for mode
up_std_dev = np.std(up_fractal_rotations)
up_1st_std_dev_high = up_mode + up_std_dev
up_2nd_std_dev_high = up_mode + 2 * up_std_dev

# Down Fractals
down_fractal_rotations = data['Low'] - data['fractal']
down_fractal_rotations = down_fractal_rotations[down_fractal_rotations != 0]
down_mode = np.mean(down_fractal_rotations)  # Use mean for mode
down_std_dev = np.std(down_fractal_rotations)
down_1st_std_dev_low = down_mode - down_std_dev
down_2nd_std_dev_low = down_mode - 2 * down_std_dev

# Output (Enhanced)
print(f"Harmonic Rotations Study:")
print(f"-------------------------")
print(f"Up Mode: {up_mode:.2f}")
print(f"Up 1st Std Dev High: {up_1st_std_dev_high:.2f}")
print(f"Up 2nd Std Dev High: {up_2nd_std_dev_high:.2f}")
print(f"Down Mode: {down_mode:.2f}")
print(f"Down 1st Std Dev Low: {down_1st_std_dev_low:.2f}")
print(f"Down 2nd Std Dev Low: {down_2nd_std_dev_low:.2f}")