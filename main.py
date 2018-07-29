import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)

from itertools import product
import seaborn as sns
import matplotlib.pyplot as plt

#input dateset
items = pd.read_csv('../input/items.csv')
shops = pd.read_csv('../input/shops.csv')
cats = pd.read_csv('../input/item_categories.csv')
train = pd.read_csv('../input/sales_train.csv')

# set index to ID to avoid droping it later
test  = pd.read_csv('../input/test.csv').set_index('ID')