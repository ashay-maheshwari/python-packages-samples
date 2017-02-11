import pandas as pd

world_cup_winners = {'year':[2015, 2011, 2007, 2003, 1999, 1996, 1992], 
                     'team':['Australia', 'India', 'Australia','Australia', 'Australia', 'Sri Lanka', 'Pakistan']
                    }
worldcup_winners = pd.DataFrame(world_cup_winners, columns=['year','team'])
print worldcup_winners




