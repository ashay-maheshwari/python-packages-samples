import pandas as pd

# Init Dictionary and convert it into Series 
player_stats = {'V Kohli':654, 'R Sharma':674, 'S Dhawan': 433, 'A Rahane':345}
player_stats_series = pd.Series(player_stats)
print player_stats_series

# Change value based on index
print('Old Value of A Rahane: ',player_stats_series['A Rahane'])
player_stats_series['A Rahane'] = 456
print('New Value for A Rahane: ',player_stats_series['A Rahane']) 
