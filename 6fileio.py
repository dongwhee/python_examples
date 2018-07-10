# -*- coding: utf-8 -*-
# mode r: read, w: write(overwritten), a: append, r+: read+write

# 테스트 하기 전에 경로를 본인에게 맞게 변경해야 합니다.
file_path = '~/Courses/gist/2python/data.txt'

f = open(file_path, 'r')
data = f.read()
print data
f.close()

with open(file_path, 'r') as f:
    data = f.read()
    print data

from datetime import date
with open(file_path, 'a') as f:
    today = date.today()
    f.write(str(today) + '\n')

# 현재 시간을 저장해보자
