#!/usr/bin/env python

a = 'pre-defined '
b = 'variables '
c = 'from global'

def fun(x, y, z):
    return x + y + z

d1 = {
  'x' : 'Diction', 
  'y' : '-ary', 
  'z' : 'Words'
}
my_list = ['variables ', 'from ', 'list']
#
return_val = fun(*my_list)
print 'This is printing the function from my list {}.'.format(return_val)
#
return_val = fun(a, b, c)
print 'This is printing the function from my passed arguments {}.'.format(return_val)
#
return_val = fun(**d1)
print 'This is printing the function from my dictionary {}.'.format(return_val)
