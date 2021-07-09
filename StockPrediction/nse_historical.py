
# git clone https://github.com/NSEDownload/NSEDownload
# pip3 install NSEDownload/dist/NSEDownload-3.0.0.tar.gz
# pip3 install python-Levenshtein

from NSEDownload import stocks
df = stocks.get_data(stockSymbol="INFY", start_date = '31-12-2018', end_date = '2-6-2021')
print(df.shape)
print(df.head())
print(df.columns)
