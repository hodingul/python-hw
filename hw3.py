# -*- coding: utf-8 -*-
"""hw3.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bp8U87jU1Wtu_gWtNn4iQjPd1CWWD7-0
"""

###discountrate.py
def set_discount_rate(dis_rate):
  global discount_rate
  discount_rate = dis_rate

def get_fixed_price(dis):
  return dis / ((100 - discount_rate) / 100)

import discountrate as Drate

dis_rate = int(input('할인율은?'))
Drate.set_discount_rate(dis_rate)
Adis = int(input('A상품의 할인된 가격은?'))
Bdis = int(input('B상품의 할인된 가격은?'))
print('A 상품의 정가는', Drate.get_fixed_price(Adis), '원')
print('B 상품의 정가는', Drate.get_fixed_price(Bdis), '원')