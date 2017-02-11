import pandas as pd

# Init Dictionary and convert it into Series 
player_stats = {'V Kohli':654, 'R Sharma':674, 'S Dhawan': 433, 'A Rahane':345}
player_stats_series = pd.Series(player_stats)
print player_stats_series


# search an intem in series 
print('V Kohli' in player_stats_series)
