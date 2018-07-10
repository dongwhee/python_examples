# -*- coding: utf-8 -*-
# openpyxl 모듈을 설치 해야 합니다.
# pip install openpyxl
from openpyxl import load_workbook

# 테스트 하기 전에 경로를 본인에게 맞게 변경해야 합니다.
file_path = '/Users/naaveh/Courses/gist/2python/sample.xlsx'
wb = load_workbook(filename = file_path)
sheet = wb.active
#sheet_ranges = wb['SHEET_TITLE']
print sheet['B1'].value
#sheet.title = 'gist'

stock_sum = 0
for col in ['B', 'C', 'D', 'E']:
    cell = col + str(3)
    value = sheet[cell].value
    stock_sum += value
print 'stock: ', stock_sum

sheet['F3'] = stock_sum
wb.save(filename = file_path)

# 각 과일의 모든 가격과 총 합을 저장해보자
