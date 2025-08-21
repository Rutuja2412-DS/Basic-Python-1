# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 22:40:34 2025

@author: admin
"""

cities=["mumbai","new york","paris"]
countries=["India","USA","France"]
z=zip(cities,countries)
z
for i in z:
    print(i)
##Instead of that:
d={city:country for city,country in zip(cities,countries)} 
print(d)   

##Try Catch:
try:
     num1=float(input('enter number1  '))
     num2=float(input('enter number2  '))  
     num=num1/num2
     print("the result is num",num)
except ZeroDivisionError:
     print("Error:Division by zero is not allowed.")
except ValueError:
     print("Error:please enter numeric values only.")
     num1=float(input(""))     

a=10
b=0
result=a/b    

try:
    result=a/b
except ZeroDivisionError:
    print("cannot divide by zero!")
    
number=[1,2,3]
print[number[5]] 
##
number=[1,2,3]   
try:
    print( number[5])
except IndexError:
    print("Index out of range")
###
try:
    numerator=50
    denominator=int(input("enter a denominator  "))
    quotient=(numerator/denominator)
    print("division perfomed successfully")
except ValueError:
    print("only integer should be entered")
except:
    print("oops.... some exceptiona are raised")
      
##handling exception using try..except..else..:
try:
    numerator=50
    denominator=int(input("enter a denominator  "))
    quotient=(numerator/denominator)
    print("division perfomed successfully")
except ZeroDivisionError:
    print("denominator 0 is not allowed!")
except ValueError:
    print("onlly integer number allowed")
else:
    print("the result of division is quotient ",quotient)    
  
##handling exception using try..except..else..finally:    
try:
    numerator=50
    denominator=int(input("enter a denominator  "))
    quotient=(numerator/denominator)
    print("division perfomed successfully")
except ZeroDivisionError:
    print("denominator 0 is not allowed!")
except ValueError:
    print("onlly integer number allowed")
else:
    print("the result of division is quotient ",quotient)
finally:
    print("over and out")
    
###File Not Found Error:
with open('c:/1-python/pi_digits.txt','r') as file:
    contents = file.read()
print(contents) 
###
try:
    with open('c:/1-python/pi_digits.txt','r') as file:
        contents = file.read()
except FileNotFoundError:
    print("File Not Found")    
    
####Permission Error:
with open('c:/1-python/pi_digits_new.txt') as file:
    contents = file.read()
print(contents.rstrip())
####     
try:
    with open('c:/1-python/pi_digits_new.txt') as file:
        contents = file.read()
    print(contents.rstrip())    
except PermissionError:
    print("you dont have permision to access this file!")
      
####Attribute Error:
object=None
print(object.some_attribute) 
##
if object is not None:
    print(object.some_Attribute)
else:
    print("object is None")   
   
##Memory Error:
huge_list=[1]*(10**10)    
####
try:
    huge_list=[1]*(10**10)
except MemoryError:
    print("there is memory overflow!")
  
###Handling using generator:
def generate_numbers():
    for i in range(10**10):
        yield i
gen= generate_numbers() 
print(next(gen)) 

##Stop Iteration Error: 
gen =generate_numbers()
for i in range(10**10+1):
    print(next(gen))
    
##Type Error:
gen=[1,2,3]
print(next(gen))   

##Handling Error:
def generate_numbers():
    for i in range(10**10):
        yield i
gen=generate_numbers()
try:
    print(next(gen))
except StopIteration:
    print("Generator is exhausted")
except MemoryError:
    print("Memory error occured")
except Exception as e:
    print("Some unexpected error occured",e)
finally:
    print("Finished Execution")  
    
###Recursive Function:
def recursive_function():
    return recursive_function()
recursive_function()

###
import sys
sys.setrecursionlimit(1000)
def safe_recursive_function(depth=0,max_depth=10):
    if depth>=max_depth:
        return "Done"
    return safe_recursive_function(depth+1,max_depth)
print(safe_recursive_function())
    

###Use Case:
balance=500
def withdraw(amount):
    global balance
    
    try:
        if not isinstance(amount,(int,float)):
            raise TypeError("Invalid amount type!plz enter")
        
        if amount<=0:
            raise ValueError("Withdrwal amount must be greater")
        
        if amount >balance:
            raise ValueError("Insufficient balance")
          
        ###Deduct Amount    
        balance=-amount
        print(f"withdrawal sucessfully new balance: ${balance:.2f}")
        
    except TypeError as e:
        print(f"Error:{e}")
    except ValueError as e:
        print(f"Transaction failed:{e}")
    except Exception as e:
        print(f"unexpected Error:{e}")
    
withdraw(500)
withdraw("Fifty")    
withdraw(-50)    
withdraw(1000)    

###
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

##using comprehension
lst=[num for num in range(0,20)]
print(lst)
    
 ###
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names] 
print(lst)  
    
###list comprehension using even no
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if  is_even(num)]
print(lst)

##for inside for:
lst=[f"{x}:{y}" for x in range(3) for y in range(3)]
print(lst)

##set comprehension:
set_one={x for x in range(3)}
print(set_one)
 
##dict comprehension:
dict={x:x*x for x in range (3)}
print(dict) 
   
##Generator:
gen=(x for x in range (3) )
print(gen)     
for num in gen:
    print(num)
    
##
gen=(x
     for x in range(3)
     )  
next(gen) 

###
gen=(x for x in range(3))
next(gen)
next(gen)   
next(gen)

##Function which return multiple value:
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
    
##Instead of using for loop we can write oue own generator:
gen=range_even(6)
next(gen)
next(gen) 
next(gen)

###Let's hide password entered on screen:
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
    
##
passwords=["not-good","give'm-pass","00100-100"]    
for password in  hide(lengths(passwords)):
    print(password)
    
##Enumerator:
lst=["Milk","Egg","Bread"]
for index in range (len(lst)):
    print(f'{index+1} {lst[index]}') 
    
##Same code using Enumerator:
lst=["Milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
    
###ZIP Function()
name=["dada","mama","kaka"]
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)  
    
##Zip function with mismatch list:
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)  
    
###Zip Longest:
from itertools import zip_longest 
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)    
    
###Use of Fillvalue instead of None:
from itertools import zip_longest 
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)    
    
##Use of ALL()
lst=[2,3,-6,8,9]
if all(lst):
    print("all values are true")
else:
    print("there are null value")
    
###
lst=[2,3,-6,0,9]
if all(lst):
    print("all values are true")
else:
    print("there are null value")    
    
###Use of any if any one non-zero value:
lst=[0,0,0,-2,0]
if any(lst):
    print("It has some non zero value")
else:
    print("useless")   

##
def is_even(num):
    return num %2==0
lst=[num for num in range(1) if is_even(num)]
print(lst)

###Use of any
lst=[0,0,0,0,0]
if any(lst):
    print("It has some value")
else:
    print("all values are null in the list")
 
###Count():
from itertools import count
counter=count()
print(next(counter)) 
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

## Now let us start from 1
from itertools import count
counter=count(start=1)
print(next(counter)) 
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) 

##Cycle():
import itertools
instructions=("Eat","code","sleep")
for instructions in itertools.cycle(instructions):
    print(instructions)
    
##Repeat():
    
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)
    

#

##combination:
from itertools import combinations
players=['john','jani','janardhan']
for i in combinations(players, 2):
    print(i)
    
  
###permutation:
from itertools import permutations
players=['john','jani','janardhan']
for seat in permutations(players, 2):
    print(seat)    
    
##product:
from itertools import product    
team_a=['saurabh','rutuja','snehal'] 
team_b=['Gauri','seema','Meena']  
for pair in product(team_a,team_b):
    print(pair)

##Reading CSV data as Lists
import csv
with open('c:/1-python/buzzers.csv')as raw_data:
    for line in csv.reader(raw_data):
        print(line)

##Reading CSV Data As Dictionaries:
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
        
###
with open('buzzers.csv') as data:
    ignore=data.readline()
    for line in data:
        flights=line.strip( ).split(",")
        print(flights)
        
        
#Decorators:
def plus_one(number):
    number1=number + 1
    return number1
plus_one(5)        

##defining function inside other function:
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(4)

##Passing Function as argument:
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)   

##Function Returning other function:
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

hello=hello_function()
hello()

##Need of decorators:
def calc_square(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for excution square is {total_time}")
    return result

def calc_cube(numbers):
    start=time.time()
    result= []
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for excution square is {total_time}")
    return result

array=range(1,100000)
out_square=cal_square(array) 
out_cube=cal_cube(array)


##by using decorators:
def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
decorate = uppercase_decorator(say_hi)
decorate()



###
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


####multiple decorators in 1 function:
def split_string(function):
    def wrapper():
        func=function()
        splitted_String=func.split()
        return splitted_String
    return wrapper 

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper 

@split_string 
@uppercase_decorator 
def say_hi():
    return 'hello there'
say_hi()

###
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func._name_+"took"+
              str((end-start)*1000)+"mil sec")
        return result
    return wrapper
 
@time_it    
def calc_square(numbers):
    result= []
    for number in numbers:
        result.append(number*number)
        return result
    
@time_it    
def calc_cube(numbers):
    result= []
    for number in numbers:
        result.append(number*number*number)
        return result    
    
array=range(1,100000)   
out_square=cal_square(array) 
out_cube=cal_cube(array)

##Find out prime no:
def is_prime(num):
    if num<2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
    return True
import sys
if(len(sys.argv)!=11):
    print("enter 10 numbers") 
else:
    numbers=list(map(int,sys.argv[1:])) 
    sum_prime=sum(i for i in numbers if is_prime(i))
    print(sum_prime) 



#####OOP'S
class Vehicle:
    def general_usage(self):
        print("general use:transportation")
        
class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels=4
        self.has_roof=True
        
    def specific_usage(self):
        self.general_usage()
        print("specific use:commute to work,vacation with famoly")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am motorcycle")
        self.wheels=2
        self.has_roof=False
        
    def specific_usage(self):
        self.general_usage()
        print("Specific use:local commutation,racing")
        
c=Car()
m=MotorCycle()
c.specific_usage()
m.specific_usage()        

## class:
class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
    
    def circumference(self):
        return 2 * 3.14 * self.r

    def area(self):
        return 3.14 * self.r * self.r
##Creating an object of circle:
a_circle=Circle(2.0,2.0,1.0)
b_circle=Circle(3.0,3.0,2.0)
##accessing data and methods:
print("Radius:", a_circle.r)
print("circumference:", a_circle.circumference())
print("Area:", a_circle.area())    
    

##Encapsulation:
class Circle:
    def __init__(self,x,y,r):
        self.__x = x
        self.__y = y
        self.__r = r   
    
    def get_radius(self):
        return self.__r
    
    def set_radius(self,r):
        if r>0:
            self.__r=r
        else:
            print("Invalid Radius")
            
c2=Circle(1,1,3)
print(c2.get_radius())
            
####Inheritance:
class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r       
    def area(self):
        return 3.14 * self.r ** 2
    
    def circumference(self):
        return 2*3.14*self.r
    
    def display_info (self):
        print(f"Center:({self.x},{self.y}),Radius:{self.r}")
        print(f"Area:{self.area():.2f}")
        print(f"Circumference:{self.circumference():.2f}")
#Derived Class:
class ColoredCircle(Circle):
    def __init__(self,x,y,r,color):
        super().__init__(x,y,r)
        self.color=color
##Overrriding the display_info method:
    def display_info(self):
        super().display_info()
        print(f"Color:{self.color}")
c1=ColoredCircle(0,0,5,"Red")
c1.display_info()        
        
###Polymorphism:
class Calculator:
     def add(self,a,b=0,c=0):
         return a+b+c

calc=Calculator()
print(calc.add(5))
print(calc.add(5,3))
print(calc.add(5,3,2))

###Method Overriding:
class Animal:
    def speak(self):
        print("Animal speaks")
 
class Dog(Animal):
    def speak(self):
        print("Dog barks")
        
class Cat(Animal):
    def speak(self):
        print("cat Meows")      
##polymorphism in action:
for animal in [Dog(),Cat()]:
    animal.speak()
        
##Another Example of Method Overriding:
class Circle:
     def area(self):
         return "calculating area of circle"

class square:
     def area(self):
         return"calculating area of square"
 
shapes=[Circle(),square()]
for shape in shapes:
    print(shape.area())   
    
#####Abstraction:
from abc import ABC ,abstractmethod
#Abstact class
class Vehicle(ABC):
 
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def start(self):
        pass
##Concrete class
class car(Vehicle):
     def start(self):
         print("car started")
         
     def stop(self):
         print("car stopped")
       
v=car()
v.start()
v.stop()        
         
###         
from abc import ABC ,abstractmethod
#Abstact class
class Shape(ABC):
 
    @abstractmethod
    def area(self):
        pass    
    
class Circle(Shape):
     def __init__(self,r):
         self.r=r
         
     def area(self):
         return 3.14 * self.r **2
     
c4=Circle(4)
print("Area:",c4.area())
 
###
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def greet(self):
        print(f"Hello,my name is{self.name}and I am {self.age}year old")
##Object:
person1=person("alice",50)
person1.greet()        
    
###
class BankAccount:
     def __init__(self,owner,balance):
         self.owner=owner
         self._balance=balance
         
     def deposit(self,amount):
         if amount > 0:
             self._balance += amount
            
     def withdraw(self,amount):
         if 0 < amount <=self.__balance:
             self.__balance -=amount
         else:
             print("Insufficient funds")
             
     def get_balance(self):
         return self.__balance
        
acc=BankAccount("Ravi", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())
print(acc.___balance)        
        
####        
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
        
    def deposit(self,amount):
        if amount >0:
            self.__balance+=amount
      
    def get_balance(self):
        return self.__balance

ba1=BankAccount(300)
print(ba1.get_balance())
ba1.deposit(100)
print(ba1.get_balance())    

###Multiple Inheritance:
class father:
    def skills(self):
        print("father:gardening,cooking")
        
class mother:
    def skills(self):
        print("mother:painting,singing")
        
class child(father,mother):
    def skills(self):   
        
        father.skills(self)
        mother.skills(self)
        print("child:coding")
c=child()
c.skills()        
        
###Hierarchical Inheritance:
class father:
    def show_skills(self):
        print("father:gardening,cooking")        
        
class child1(father):
    def show_child1_skills(self):
        print("child1:Drawing,football")
        
class child2(father):
    def show_child2_skills(self):
        print("child2:singing,chess")  
        
c1=child1()
c1.show_skills()
c1.show_child1_skills() 

c2=child2()
c2.show_skills()
c2.show_child2_skills()      


#######Data Science:
import pandas as pd
songs2=pd.Series([145,142,38,13],name='counts') 
songs2.index

songs3=pd.Series([145,142,38,13],name='counts',
                 index=['paul','john','george','ringo'])
songs3.index
songs3

##
import pandas as pd
f1=pd.read_csv('age1.csv')
f1

df=pd.read_excel('c:/2-python_DS/Bahaman.xlsx')

##Numpy
import numpy as np
numpy_ser=np.array([145,142,38,13])
songs3[3]
numpy_ser[0]
numpy_ser[1]
numpy_ser[2]

songs3.mean()
numpy_ser.mean()

##
george=pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'],
name='George_Songs')
george
george['1968']
george['1969']
george['1970']

for item in george:
    print(item)

##Updating:
george['1969']=68
george['1969']
george

##Deletion:
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

##cONVERT Types:
songs_66=pd.Series([3,None,11,9],
index=['george','ringo','john','paul'],
name='Counts')
songs_66.dtypes

pd.to_numeric(songs_66.apply(str))
pd.to_numeric(songs_66.astype(str),errors='coerce')

songs_66.dtypes

songs_66=songs_66.fillna(-1)
songs_66=songs_66.astype(int)
songs_66.dtypes

songs_66=pd.Series([3,None,11,9],
index=['george','ringo','john','paul'],
name='Counts')
songs_66=songs_66.dropna()
songs_66


##Append ,joining
songs_69=pd.Series([7,16,21,39],
index=['ram','sham','ghansham','krushna'],
name='Counts')

songs=pd.concat([songs_66,songs_69])
songs

####Plotting Series:
import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot()
plt.legend()    

###
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()

###
import numpy as np
data=pd.Series(np.random.randn(500),name='500_random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()

##
import pandas as pd
pd.__version__

##Creating dataframe  using list
import pandas as pd
technologies=[["spark",20000,"30days"],
              ["pandas",20000,"40days"]] 
df=pd.DataFrame(technologies)
print(df)   

###
column_names=["Courses","fee","duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
df.dtypes


###
import pandas as pd
technologies={
    'courses':["spark",'pyspark',"hadoop","python",'pandas',"oracle","java"],
    'fee':[2000,23000,260000,24000,27000,29000,30000],
    'Duration':['30day','40days','35days','40days','60days','50days','55days'],
    'discount':[11.8,35.6,45.5,48.2,58.6,47.8,47.9]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)

####
df2=df.convert.dtypes()
print(df2.dtypes)

###
df=df.astype(str)
print(df.dtypes)

##
df=df.astype({"fee":int,"discount":float})
print(df.dtypes)
