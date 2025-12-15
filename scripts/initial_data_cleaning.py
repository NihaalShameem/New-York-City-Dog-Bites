'''
=======================================================================
PYTHON INITIAL DATA CLEANSING
=======================================================================
This notebook performs initial data cleaning and preprocessing on the NYC Department of Health and Mental Hygiene (DOHM) Dog
Bite dataset, sourced from NYC Open Data. The raw dataset contained inconcistent data types, extremely dirty Age Column, and 
unecessary fields.

Key Cleaning Steps Performed:
1. Data Loading & Inspection: Imported raw CSV data and performed intital EDA using .info() and .describe() to identify data 
quality issues.
2. Feature Selection: Dropped the 'Species column as it provided redundant information (all entries are dogs).
3. Data Type Optimization:
   - Converted low-cardinality columns ('Breed', 'Gender', 'SpayNeuter', 'Borough') to the 'category' data type to optimize
     memory usage.
   - Converted 'DateOfBite' to datetime objects for time-series analysis.
4. Age Column Remediation: 
   - Sanitized strings by removing non-numeric characters (e.g., 'Y').
   - Coerced invalid entries to NaN and handled infinite values.
   - Imputed missing or null values with '-1' to maintain integer integrity while flagging unknown ages.

'''

# Import necessary packages for data cleaning
import pandas as pd
import numpy as np
import datetime as dt

# Load the dataset
# Note: Update with your own path with downloaded dataset from DOHM Websited
data = pd.read_csv(r'')

# --- Initial Inspection ---
print("Initial Data Info:")
data.info()
print("\nInitial Description:")
print(data.describe(include=['object','bool']))

# --- Data Cleaning ---

# 1. Feature Selection: Drop redundant column
data = data.drop(columns= ["Species"])

# 2. Data Type Optimization
# Convert to category to save space
data[['Breed','Gender','SpayNeuter','Borough']] = data[['Breed','Gender',
                                                        'SpayNeuter','Borough']].astype('category') 

# Change the date column to datetime
data['DateOfBite'] = pd.to_datetime(data['DateOfBite'])

# 3. Clean 'Age' Column
# Remove 'Y' and convert to numeric
data['Age'] = data['Age'].astype(str).str.replace('Y','', regex=False)
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

# Handle invalid values (inf) and fill NaNs with -1
data['Age'] = data['Age'].replace([np.inf, -np.inf], np.nan)
data['Age'] = data['Age'].fillna(-1).astype(int)

# 4. Clean 'Breed' and 'ZipCode' (Handle Blanks)
# Replace empty strings or whitespace with np.nan (Null)
data['Breed'] = data['Breed'].replace(r'^\s*$', np.nan, regex=True)
data['ZipCode'] = data['ZipCode'].replace(r'^\s*$', np.nan, regex=True)


# --- Final Checks ---
print("\nUnique Ages after cleaning:")
age_unique = sorted(data['Age'].unique())
print(*age_unique)

print("\nNull Value Counts after cleaning blanks:")
print(data[['Breed', 'ZipCode']].isnull().sum())

# Display first few rows of the cleaned data
data.head()

# Downloading to CSV to then upload into SQL for futher analysis
# Update the below code with your own path to download as CSV
file_path = r''
data.to_csv(file_path)


