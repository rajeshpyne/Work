import pandas as pd
import numpy as np


def read_df():
    users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',delimiter='|')
    # print(users.info())
    print(users.head())
    ## Mean Age per occupation
    cf =users.groupby('occupation').mean()
    print(cf.age)
    ## Male Ratio per occupation and sort by Descending
    occ_count = (users.groupby('occupation').count())
    print(occ_count)
    rdf = users.loc[users.gender == 'M'].count() /occ_count
    print(rdf[['gender']])


if __name__ == '__main__':
    read_df()