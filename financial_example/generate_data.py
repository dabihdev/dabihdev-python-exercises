import pandas as pd
import numpy as np

# Create mock data for 3 regions
regions = ['North', 'South', 'West']
for region in regions:
    data = {
        'Date': pd.date_range(start='2026-01-01', periods=5, freq='ME'),
        'Department': ['Sales', 'Marketing', 'Ops', 'IT', 'HR'],
        'Budget': np.random.randint(10000, 20000, size=5),
        'Actual': np.random.randint(9000, 22000, size=5)
    }
    df = pd.DataFrame(data)
    df.to_csv(f'Monthly_Report_{region}.csv', index=False)

print("Mock CSV files created: North, South, and West.")