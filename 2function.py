#!/usr/bin/env python
def say_hello():
    print 'Hello'

say_hello()

def say(message, times=1):
    print(message * times)
    print 'times', times

say('hello')
say('gist', 5)
say('gist', times=3)

#
# create check function from 1flow.py source
#
def check(a, b):
    print 'a is b', a is b
    print 'a == b', a == b

a = [1, 2, 3]
b = a
check(a,b)
b = a[:]
check(a,b)
