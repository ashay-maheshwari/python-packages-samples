import pandas as pd
import numpy as np

# Init Dictionary and convert it into Series 
player_stats = {'V Kohli':654, 'R Sharma':674, 'S Dhawan': 433, 'A Rahane':345}
player_stats_series = pd.Series(player_stats)
print player_stats_series

# Divide all values by 5 
print player_stats_series/5

# Square city values
print np.square(player_stats_series)
