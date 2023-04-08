# -*- coding: utf-8 -*-
"""hw5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_15tDKfTULCVWBaSKUG49TjQkZ3IPebn
"""

def read_single_digit(n):
  if n == 0 :
    return '영'
  elif n == 1 :
    return '일'
  elif n == 2 :
    return '이'
  elif n == 3 :
    return '삼'
  elif n == 4 :
    return '사'
  elif n == 5 :
    return '오'
  elif n == 6 :
    return '육'
  elif n == 7 :
    return '칠'
  elif n == 8 :
    return '팔'
  elif n == 9 :
    return '구'

def read_number(num):
  n1 = num // 100
  N = num % 100
  n2 = N // 10
  n3 = N % 10
  N1 = read_single_digit(n1)
  N2 = read_single_digit(n2)
  N3 = read_single_digit(n3)
  return f'{N1} {N2} {N3}'

number = int(input('세 자리 정수 입력: '))
print(read_number(number))