#
# If statement
#
number = 23
guess = 30

if guess == number:
    print 'correct'
elif guess < number:
    print 'higher'
else:
    print 'lower'

if guess is not number:
    print 'incorrect'

a = [1, 2, 3]
b = a
print 'b is a', b is a
print 'b == a', b == a
b = a[:]
print 'b is a', b is a
print 'b == a', b == a

str1 = 'hello'
str2 = str1
str3 = 'hello'

if str1 == str2:
    print 'str1 == str2'
if str1 is str2:
    print 'str1 is str2'
if str2 == str3:
    print 'str2 == str3'
if str2 is str3:
    print 'str2 is str3'

#
# For loop
#
print 'for ---------------'

for i in range(1,5):
    print i

print 'for2 ---------------'

for i in range(3, 100, 3):
    print i

#
# While
#
print 'while ---------------'
a = 0
while a < 10:
    a += 1
    print a

print 'while2 ---------------'
while True:
    if a < 5:
        break
    print a
    a -= 1
