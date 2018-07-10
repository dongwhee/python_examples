#
# Array
#
arr = [0, 1, 2, 3]
print arr

arr2 = range(0, 4)
print arr2

print range(3, 100, 3)
print len(range(3, 100, 3))

# edit array
arr3 = ['h', 'e', 'l', 'l', 'o']
arr3.append('!')
print arr3
arr3.remove('!')
print arr3
#arr3.remove('l') -> ??

# split array
arr3 = ['h', 'e', 'l', 'l', 'o']
print arr3[0] # 'h'
print arr3[2:4] # 'l', 'l'
print arr3[2:-1] # 'l', 'l'

#
# Dictionary (key-value set)
#
d = { 'a': 10, 'b': 20, 'c': 30}
print d
print 'a =', d['a']
d['a'] = 30
print 'a =', d['a']

#
# tuple
#
t = (10, 'hello', .5)
print t
print t[0]
a, b, c = t
print b
