import pandas as pd

df = pd.read_csv('~/election_stuff/election_data/county_data/pres_election_2004_county.csv')
df_county = pd.read_csv('~/election_stuff/election_data/county_data/county_codes.csv')


county_list = df_county["Name"].to_list()

print(df[df['county'].str.match('Autauga')])




def create_csv_files():
    i = 2000
    while(i<2017):
        df_temp = df[df['year'] == i]
        print(df_temp.head(n=4))
        print(df_temp.tail(n=4))
        file_str = '~/election_stuff/election_data/county_data/pres_election_'+str(i)+'_county.csv'
        df_temp.to_csv(file_str, index=False)
        i+=4

