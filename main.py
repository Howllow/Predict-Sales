import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)

from itertools import product
import seaborn as sns
import matplotlib.pyplot as plt

#input dateset
items = pd.read_csv('/input/items.csv')
shops = pd.read_csv('/input/shops.csv')
cats = pd.read_csv('/input/item_categories.csv')
train = pd.read_csv('/input/sales_train.csv')

# set index to ID to avoid droping it later
test  = pd.read_csv('/input/test.csv').set_index('ID')

#remove outliers
train = train[train.item_price < 100000]
train = train[train.item_cnt_day < 1001]

#deal with the item whose price is below zero
median = train[(train.shop_id == 32) & (train.item_id == 2973) & (train.date_block_num == 4) & (train.item_price > 0)].item_price.median()
train.loc[train.item_price < 0, 'item_price'] = median

#some shops are duplicates of each other, we should change their id

# Якутск Орджоникидзе, 56
train.loc[train.shop_id == 0, 'shop_id'] = 57
test.loc[test.shop_id == 0, 'shop_id'] = 57

# Якутск ТЦ "Центральный"
train.loc[train.shop_id == 1, 'shop_id'] = 58
test.loc[test.shop_id == 1, 'shop_id'] = 58

# Жуковский ул. Чкалова 39м²
train.loc[train.shop_id == 10, 'shop_id'] = 11
test.loc[test.shop_id == 10, 'shop_id'] = 11


