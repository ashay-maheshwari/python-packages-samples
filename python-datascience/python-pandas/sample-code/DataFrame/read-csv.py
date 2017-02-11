import pandas as pd


# Import data frame by reading a csv file .
# The first row of csv file is considered to be the header of the data frame
from_csv = pd.read_csv('test-data.csv')
print from_csv

# To override the default behavior 
from_csv = pd.read_table("test-data.csv", header=None).head()
print from_csv


# use read table command to read-csv
from_csv = pd.read_table("test-data.csv", sep=',')
print from_csv
