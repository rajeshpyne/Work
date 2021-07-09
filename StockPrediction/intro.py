from nsetools import Nse

nse = Nse()
print(nse)

## Getting a stock quote
q = nse.get_quote('RELIANCE')
print(q)

# ## Index Quote
# index =nse.get_index_list()
# print(index)
# id_quote =nse.get_index_quote('india vix')
# print(id_quote)
#
# ## List of traded stock quotes
# all_stock_codes = nse.get_stock_codes()
# print(all_stock_codes)
#
# # Advances and Declines
# adv_dec = nse.get_advances_declines()
# print(adv_dec)
#
# # Top losers and gainers
# top_gainers = nse.get_top_gainers()
# print(top_gainers)
# top_losers = nse.get_top_losers()
# print(top_losers)
#
# #Check if the code is valid or not
# is_valid = nse.is_valid_code('rel')
# print(is_valid)
#
# is_idx_valid = nse.is_valid_index('india vix')
# print(is_idx_valid)
#
# # Getting lot sizes
# lot_size = nse.get_fno_lot_sizes()
# print(lot_size)