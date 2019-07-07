'''
Created on Jan 22, 2019

@author: chenz
'''
# coding=utf-8 
# coding=gbk
# -*- coding:utf-8 -*-
from collections import OrderedDict
import json 

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
    
    

print(json.dumps(d))


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


min_price = min(zip(prices.values(), prices.keys()))
print("min price is :  " )
print(min_price)
 

min_name = min(zip(prices.keys(), prices.values()))
print("min name is :  " )
print(min_name)
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print("max price is :  " )
print(max_price)
# max_price is (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print("sort with price")
print (prices_sorted)




prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
#print(max(prices_and_names)) # ValueError: max() arg is an empty sequence