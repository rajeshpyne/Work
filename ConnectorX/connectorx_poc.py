import connectorx as ctx
import pandas as pd
import time
from sqlalcehmyPOC.database import engine,SQL_DB_URL


def time_calculate(func):
    def calc_time(*args, **kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("Execution time: "+str(end_time - start_time))
    return calc_time


@time_calculate
def convert_csv_to_parquet():
    df = pd.read_csv('Sales_records.csv')
    df.to_parquet('Sales_Records.parquet', compression='brotli', engine='pyarrow')


@time_calculate
def read_df():
    pq_df = pd.read_parquet('Sales_Records.parquet',engine='pyarrow')
    pq_df.columns = pq_df.columns.str.lower()
    pq_df.columns = pq_df.columns.str.replace(' ', '')
    codes, uniques = pd.factorize(pq_df.country)
    # print(codes, uniques)
    pq_df['country_code'] = codes
    # print(pq_df.info())
    # pq_df.to_csv('Sales_records.csv',header=True,index=False)
    pq_df.to_sql('sales_records',engine,schema='public',if_exists='replace',index=False)


@time_calculate
def read_concentrix():
    df = ctx.read_sql(SQL_DB_URL, "SELECT * FROM public.sales_records limit 3000000")
    print(df.head())


@time_calculate
def read_df_direct():
    df = pd.read_sql('select * from public.sales_records limit 3000000', engine)
    print(df.head())


if __name__=='__main__':
    # convert_csv_to_parquet()
    # read_df()
    read_concentrix()
    # read_df_direct()