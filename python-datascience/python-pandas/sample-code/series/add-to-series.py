import pandas as pd
import numpy as np

# Init Dictionary and convert it into Series for first tournament
player_stats = {'V Kohli':654, 'R Sharma':674, 'S Dhawan': 433, 'A Rahane':345}
player_stats_series1 = pd.Series(player_stats)
print "Player Statistics in first tournament\n",player_stats_series1

# Init Dictionary and convert it into series for second tournament 
player_stats = {'V Kohli':564, 'R Sharma':654, 'S Dhawan': 733, 'A Rahane':745}
player_stats_series2 = pd.Series(player_stats)
print "Player Statistics in Second tournament\n",player_stats_series2

# Adding series together 
new_series = player_stats_series1 + player_stats_series2
print "After adding two series \n",new_series

