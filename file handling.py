# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 17:31:52 2025

@author: admin
"""
with open('c:/1-python/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)    

with open('d:/1-python/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip()) 

file_path='c:/1-python/pi_digits.txt'
with open(file_path) as file_object:
    contents=file_object.read()
print(contents.rstrip())    
 
filename='c:/1-python/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
        
filename='c:/1-python/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())  
        
filename='c:/1-python/pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())        
        
filename='c:/1-python/pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string+=line.rstrip()
        print(pi_string)
        print(len(pi_string))
        
filename='c:/1-python/programming.txt'
with open(filename,'w') as file_object:
    file_object.write("i love programming.\n")
    file_object.write("i love creating new games.\n")
    
filename='c:/1-python/programming.txt'
with open(filename,'a') as file_object:
    file_object.write("i also love finding meaning in large dataset.\n")        
    file_object.write("i love creating apps that can run in a browser.\n")    