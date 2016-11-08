#!/usr/bin/env python

ip = raw_input('What is your IP Address? ')
ip_Add = ip.split('.')
print
print "{:<12}{:<12}{:<12}{:<12}".format(*ip_Add)
print
