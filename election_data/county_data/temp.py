import pandas as pd

df = pd.read_csv('~/election_stuff/election_data/county_data/county_codes.csv')

del df["stuff"]
df.to_csv('~/election_stuff/election_data/county_data/county_codes.csv', index=False)