import pandas as pd

def line():
	print "\n---------------------------------------------------------------------\n"

# Create a series with some values 
# By default a series will take index from 0 to N - 1 
s = pd.Series([8,'Ashay', 54.678, -908, 'String again'])
print s

line()

# If you want to mention some other index for Series to take 
s = pd.Series([8,'Ashay', 54.678, -908, 'String again'],index=['A', 'Z', 'C', 'Y', 'E'])
print s

line()

# Convert a Dictionary to a Series object 
d = {'V Kohli':567, 'RG Sharma': 678, 'SK Raina': 433}
s = pd.Series(d)
print s

line()

# To print a specific combination from a series 
print s[['V Kohli', 'RG Sharma']]

line()

# Perform boolean indexing using condition
print s[s > 500]


