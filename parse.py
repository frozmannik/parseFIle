import os

file_name = 'example.in'

file_path = os.path.abspath(os.path.join('data',file_name))
f = open(file_path,'r')
dict = f.readline().split() # read a first line and split value in it

print(dict)