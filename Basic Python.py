# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x=50
print(x)

x=0
x+=1
print(x)

winner=None
print(winner is None)
print(winner is not None)

a=5
b=3
print(a**b)

count=1
print('starting')
while count<=10:
    print(count)
    count+=1
    
    i = 1
while i < 6:
  print(i)
  i += 1

    
print('printout value in a range')  
for i in range(2, 10):
    print(i)
    print('done')
  
    
for i in range(5):
    print(i, end=" ")
print() 
    

start,end=4,19  
for num in range(start,end+1):
    if num%2==0:
        print(num)
 
x,y,z=5
print(x)
print(y)
print(z)



str1="hello"
str2=2
str3=str1+str2
print(f"hello{str2}")

x="""This is python.hii very"""  
print(x[2:8])  
print(x[:3])
print(x[4:])

s="python"
print(s[-5:-2])

x="""This is python.it is very powerful"""
print(x[-2:-5])
print(x[-26:-20])
print(x[8:-20])
x="This is python"
print(x.upper())
print(x.lower())

x=1
print(x)
print(type(x))  
x="rutu"
print(x)
print(type(x))  

age1=int(input("plz enter ur age1"))
print(type(age1))
print(age1)
age2=int(input("plz enter ur age 2"))
print(age2)
age=age1+age2
print(type(age))
print(age)

exchange_rate=1.83
print(type(exchange_rate))
print(exchange_rate)

int_value=100
float_value=1.5
string_value='85'
float_value=float(int_value)
print("int value as a float value:",float_value)
print(type(float_value))

float_value=float(string_value)
print("string value as a float value:",float_value)
print(type(float_value))

int_value=int(float_value)
print("float value as a integer",int_value)
print(type(int_value))

c1=1
c2=2j
print('c1:',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

all_ok=True
print(all_ok)
print(type(all_ok))

all_ok=False
print(all_ok)
print(type(all_ok))

status=bool(input('ok it is confirmed ?'))
print(status)
print(type(status))

home=0
away=15
print(home*away)
print(10-15)
type(10/15)
print(10/15)
print(10//15)
print(20/3)
print(20//3)
print(500%2)

x=4
x-=1
print(x)

Winner=None
print(winner is None)
print(type(None))

num=int(input("enter a num"))
if num > 0:
    print(num)

a = 33
b = 200
if b > a:
  print("b is greater than a")

 num=int(input("enter a num"))
if num>0:
    print("it is positive no")
else:
    print("it is negative no")
    
a = 200                                                                                                                                                             
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


saving=int(input("enter amount u hav saving"))
if saving==0:
    print("no saving")
    elif saving<500:
        print('good')
    elif(saving<1000):
        print('excellent')
    elif saving<1500:
        print("very nice")
    else:
        print(thx)
        
saving=int(input("enter amount u hav saving"))
if saving==0:
    elif saving<500:
        print('good')
    elif saving<1000:
        print('excellent')
    elif saving<1500:
        print("very nice")
    else:
        print(thx)
   
saving=int(input("enter amount u hav saving")) 
if saving==0:
    print("no saving")
elif saving<500: 
    print('good')
elif saving < 1000:
    print('excellent')
elif saving<1500:
    print("very nice")
else:
    print(thx)
        
hour = 15

if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")

x=2
print("start from2 to 15")
while x<=15:
    print(x)
    x+=1
  
print("printout value in a range")

for i in range(10,20):
    if i%2==0:
        print(i)     
   
print("only print code if all iteration completed")
num=int(input("enter a no to check for:"))
for i in range(0,16):
    if i==num:
        break
    print("Done")
     
for even_number in range(4,15,3):
    if even_number==0:
        print('even_number',end=' ')
          
x=int(input("enter value of x"))
y=int(input("enter value of y"))
for i in range(x,y+1):
     print(i,end=" ")
     
for number in range(4, 16+1, 5):
    print(number)     
        
x=range(6)
print(x)
print(type(x))

x="awesome"
def my_function():
    print("python is "+x)
    my_function()
    
x='awesome'
def my_function():
    x='funtastic'
    
    print("python is "+x)
    my function()
    print("python is "+x)
    
x=range(4)
print(x)
print(type(x))    
s
x={"Name":"Sauru","age":25}
print(x)
print(type(x))

str1="hello"
str2=2234  
str3=str1+str2
print(f"hello{str2}") 

  s="good morning. 
string1=s[::-2]
print(string1)    
print(s[5:8])
print(s[-1:5])
print(s[-6:-2])
print(s[::-1])
print(s[::-1])
print(s[2:-2])
print(s[1:-4])
print(s.upper()) 
print(s.lower())
print(s.rstrip())
print(s.strip())
print(s.replace("morning","afternoon"))

input_colors="red-blue-yellow"
def sorted_colors(input_colors):
    string_split=inpu t_colors.split("-")
    sort=sorted(string_split)
    sorted_String='_'.join(sort)
    print(sorted_string)
sorted_colors(input_colors)    


nested_list=[[1,2,3],['a','b','c'],[True,False]]
print(nested_list[-1][-1])

nested_list[1][1]='z'
print(nested_list)

for sublist in nested_list:
    for item in sublist:
        print(item)
        
 for sublist in nested_list:
     print(sublist)
lst=[ sublist for sublist in nested_list]
print(lst)   

flat_list=[item for sublist in nested_list for item in sublist]
print(flat_list)   

nested_list.append(["new","list"])
print(nested_list)

nested_list[0].append(4)
print(nested_list)

nested_list[1].remove('z')
print(nested_list)

tup=("cherry","cherry","banana")
print(tup)
print(tup[2])

x=('apple','banana','cherry')
x[1]='kiwi'
y=list(x)
y[1]='kiwi'
x=tuple(y)
print(x)

dict1={"brand":"maruti","model":"1234","year":2011}
print(dict1)
print(len(dict1))

dict1=dict(thisdict)
dict1

dict1.get("model")
dict1.keys()

car={"brand":"ford",
     "model":"mustang",
     "year":"1976"
     }
car.clear()
car.items()
car
dict1=dict(thisdict)
dict1

data={'b':2,"a":5,"c":1}
data.items()
sorted_by_keys=dict(sorted(data.items()))
print(sorted_by_keys)

x=car.keys()
print(x)



                                                                                                                                                                 
car["color"]="white"
car
x=car.keys()
print(x)    

car.pop("model")
print(car)

for x in  car:
    print(car[x])

car={"brand":"ford",}

for key,value in car.items():
    print(f"{key}:{value}")
    
input_colors="red-blue-green-yellow"
def sorted_colors(input_colors):
    string_split=input_colors.split("-")
    string_split
    sort=sorted(string_split)
    sort
    sorted_string='-'.join(sort)
    return sorted_string
sorted_alphabetic=sorted_colors(input_colors)
print(so\rted_alphabetic)
    
 
    x='hello world'
    string1=x[::-2]
    print(string1)
    
    string2=x[::-1]
    print(string2)
    
def is_palindrome(input):
    if input=="":
        return "you entered wrong input"
    else:
        string =input[::-1]
        if string==input:
            return True
        return False
print(is_palindrome("MAAM"))  

x="this is python and it is very powerful"
print(x.find("it"))

print(x.find("and"))  
print(x[15:17])

address='4/116 sundar apartment,suyognagar'
print(address.find('suyognagar')
print(address.find('116'))

 
x="hello"
y="world"
print(x+" "+y)

x=36
y="my name is rutuja"
print(x+y)
print

print(f"my name is rutuja and my age is {x}")

quantity=3
item_no=54
price=67
print(f"i want{quantity}price and item_no is{item_no},its price{price}")

my_order="i want {0} item and item_no is{},its number is{1},its price is{2}"

print(my_order.format(quantity,item_no,price))
quantity=2
item_no=4
price=100

text="this is fun fair and it has got big"round rigo""
text="this is fun fair and it has got big\"round rigo\""
print(text)



lst=["cherry","banana","cherry"]
print(lst)

lst=["cherry",1,1.3]
print(lst)
lst.append("mango")
print(lst)
lst.clear()
print(lst)


lst2=lst.copy()
print(lst2)
lst.count("cherry")

lst=[1,2,3]
lst1=[4,5,6]
lst=lst+lst1
print(lst)

lst.extend(lst1)
print(lst)

print(10==10)

a=20
b=10
if(a>b):
    print("a is gre then b")
else:
    print("b is gret a")
    
print(a==b)
print(a!=b)    
print(a is b)
print(a is not b)

lst=["cherry","banana","apple"]
lst.append("mango")
print(lst)

lst=["ram","sai"]
lst1=lst.copy()
print(lst1)

lst=[1,2,3]
lst1=[3,5,6,7]
lst2=lst+lst1
print(lst2)
lst.extend(lst1)
print(lst)

lst=["cherry","banana","apple"]
lst.pop(2)
print(lst)

lst=["cherry","banana","apple"]
lst.remove("banana")
print(lst)

lst=["cherry","banana","apple"]
lst.reverse()
print(lst)

lst=["cherry","banana","apple"]
lst.sort()
print(lst)


x="rutuja"
y=x[::-1]
print(y)

original_list = [1, 2, 3, 4, 5]
new_list = [x + 6 for x in original_list]
print(new_list)

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Iterating over keys
print("Iterating over keys:")
for key in person:
    print(key)

# Iterating over values
print("\nIterating over values:")
for value in person.values():
    print(value)

# Iterating over key-value pairs
print("\nIterating over key-value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")


lst=["kiwi","banana","apple"]
x=sorted(lst,key=len)
print(x)

nested_list=[[1,2,3],['a','b','c'],[True,False]]
print(nested_list[0])
nested_list[2][1]

print(nested_list[-1][-2])

nested_list[1][1]='z'
print(nested_list)

for sublist in nested_list:
    for items in sublist:
        print(items,end=" ")
        
flat_list=[item  for sublist in nested_list for item in sublist]
print(flat_list)
    
nested_list.append(['new','list'])
print(nested_list)        

nested_list[0].append(4)
print(nested_list)

tup=("cherry","cherry","banana")
print(tup)
print(tup[2])

x=("apple","banana","cherry")
x[1]="kiwi"
#convert into list
y=list(x)
y[1]="kiwi"

#convert into tuple
x=tuple(y)
print(x)

tup1=("a","b","c")
tup2=(1,2,3)
tup=tup1+tup2
print(tup)

dict={"brand":"maruti","model":"1234","year":"2000"}
print(dict)
print(len(dict))
print(type(dict))
dict.get("model")
dict.keys()


x="hello world"
string1=x[::-2]
print(string1)


our_family={
    "child":
        {"name":"rutuja",
         "DOB":"21-5-2000"
        },
        "child2":
            {
                "name":"saurabh",
                "DOB":"23/6/2451"
        }
            }
    
add=lambda a:a+10
print(add(20))      

fruit_dict={'mango':200,'apple':100,
            'graph':120,'banana':40}
sorted_by_value=min(fruit_dict,value=sorted_dict.get)
free_item_value=sorted_dict[free_item_value]
print(f"y will get lowest period item'{free_item_value}'({free_item_value}")for free") 

dict1={'apple':100,'graph':120,'mango':200,'banana':40}
sum=0
for value in dict1.value():
    sum=sum+int(value)
    print(sum)
 
total_sum=sum(int(value)for value in dict1.values()) 
print(total_sum)

i=1
while i<6:
    print(i)
    if(i==3):
        continue
    i=i+

def factorial(x):
    if x==1:
        return 1 
    else:
        return(x*factorial(x-1))
    factorial(5)
 
    # lambda function
lst=[34,12,64,55,75,13,63]
odd_list=list(filter(lambda x:(x%2==0),lst))
print(odd_list)

#merging 2 dict
dict1={'a':2,'b':3}
dict2={'c':1,'d':6}
dict1.update(dict2)
dict1
dict1=dict1|dict2
dict1

lst=[34,12,64,55,75,13,63]
sqr_list=list(map(lambda x:(x**2),lst))
print(sqr_list)

mul=lambda a,b,c:a*b*c
print(mul(5,6,2))

#ALEX:

no_banana=int(input("enter no of banana to be purched"))
lot1=int(input("what is size of lot  that vendor1 provides")) 
price1=int(input("price of lot1")) 

lot2=int(input("what is size of lot  that vendor2 provides")) 
price2=int(input("price of lot2")) 

def min_cost(no_banana,lot1,price1,lot2,price2):
    lot_a=no_banana//lot1
    print(f'lot_a:{lot_a}')

    lot_b=no_banana//lot2
    print(f'lot_b:{lot_b}')

    cost_a=lot_a*price1
    print(f'cost_a:{cost_a}')  

    cost_b=lot_b*price2
    print(f'cost_b:{cost_b}')
    min_cost = min(cost_a, cost_b)
    print(f'Minimum cost: {min_cost}')
    return min_cost

min_cost(no_banana, lot1, price1, lot2, price2)
 
import math
def min_cost(no_banana,lot1,price1,lot2,price2):
    lot_a=math.ceil(no_banana/lot1)
    lot_b=math.ceil(no_banana/lot2)
    
    print(f'lot_a(vendor 1'):{lot_a} lot(s) to cover {no_banana}
    print(f'lot_b(vendor 2'):{lot_b} lot(s) to cover {no_banana}
    
    cost_a=lot_a*price1
    cost_b=lot_b *price2
 
 
Example 2:FARAH:
    
input1=" wipro technologies"   
words=input1.split()
words
char_lists=[list(word)for word in words]
char_lists

letter_counts=[len(chars)for chars in char_lists]
letter_counts
print("character lists:",char_lists)
print("letter counts:",letter_counts)
def sum_digits(num):
    total = 0
    while num!=0:
        last_digit=num%10
        total=total+last_digit
        num=num//10
    return total
total=[ sum_digits(i)for i in letter_counts]
total
result=sum(total)
print(PIN,result)
###########
def get_pin(input1):
    words=input1.split()
    total_length=sum(len(word)for word in words)
    while total_length>=10:
        total_length=sum(int(digit)for digit in str(total_length))
    return total_length    
        
get_pin('the good the bad and the ugly')
get_pin('wipro technologies')  
get_pin("")   
get_pin(" ") 
get_pin("AI 101 @HOME")  
get_pin('machine learning and AI')
###########
total_sum=0
for i in total:
    total_sum=total_sum+i
total_sum
#if total sum is 2 digit then 
if (total_sum//10)!=0:
    total=sum_digits(total_sum)
    print(total)
else:
    print(total_sum)
###########

functions:
1.function without an argument
def my_function():
    print("hello my function")
my_function()    
    
2.function with argument
def my_function(name):
    print("hello "+name)
my_function("rutuja")  

3.functional with positional argument
def my_function(name1,name2):
    print(name1+" "+name2)
my_function("word" ,"hello")
my_function("hello","word")
    
4.Arbitrary argument(*args)
def my_function(*args):
    print(args[0]+" "+args[2])
my_function("tappu","sonu","goli")

5.kwargs 
def my_fun(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')
my_fun(first_name='papalal',mid_name='mohanlal',last_name='goyal')
        
6.default value
def my_fun(country="norway"):
    print("I am from " +country)
my_fun("india")
my_fun("dubai")
my_fun()
my_fun("brazil")

7.passing a list as an argument
fruits=["orange","banana","guava"]
def my_fun(fruits):
    for x in fruits:
        print(x)
my_fun(fruits)   

8.Return value
def my_fun(x):
    y=x+5
    return y
my_fun(2)     
9.###for multiple value###
def my_fun(x):
    y=x+10
    z=x*2
    return y,z
my_fun(5)

10.pass function
def my_fun1():
    pass
my_fun1()

10.Recursive 
function
def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
factorial(5)

11.lambda function
add=lambda a:a+10
print(add(2))
OR
mul=lambda a,b:a*b
print(mul(2,3))

1.check if a number is a strong number.

import math

def is_strong_number(num):
    # Store the original number
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total += math.factorial(digit)
        num //= 10

    return total == original

# Example usage:
number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong Number.")
else:
    print(f"{number} is not a Strong Number.")

2.check if a string is a palindrome(ignoring case and spaces)
def is_palindrome(s):
    cleaned=''.join(c.lower()for c in s if c!=' ')
    return cleaned==cleaned[::-1]
print(is_palindrome("race car"))
print(is_palindrome("madam"))
print(is_palindrome("racecarwr"))

##decreasing seq:
input1=[11,3,1,4,7,8,12,2,3,7] 
def count_decreasing_sequences(input1):
    input2=len(input1)
     
#input1=[11,3,1,4,7,8,12,2,3,7] 
 #input2=len(input1)

    count_sequences=0
    max_length=0
    current_length=1
    for i in range(1,input2):
        if input1[i]<input1[i-1]:
            current_length+=1
        else:
            if current_length > 1:
                count_sequences+=1
                max_length=max(max_length,current_length)
                current_length=1
           
    if current_length > 1:
        count_sequences+=1
        max_length=max(max_length,current_length)
        
        
#print("total decreasing sequences:",count_sequences)        
#print("longest decreasing sequence length:",max_length)        
        return count_sequences,max_length
print(count_decreasing_sequences(input1))
print(count_decreasing_sequences([11,3,1,4,7,8,12,2,3,7]))
print(count_decreasing_sequences([10,9,8,7]))    
print(count_decreasing_sequences([5,3,4,2,6,1]))    
print(count_decreasing_sequences([7,5,6,4,5,3]))

#print(total decreasing sequences(input1))
#print("longest decreasing sequences length:",max_length)    

##print(count_decreasing sequences)
            
#sum of odd no's:
#input1=[3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19] 
def sum_of_odd(input1):
    current_length=0
    current_sum=0
    max_length=0
    longest_sum=[]
    for num in input1:
        if num%2!=0:
            current_length+=1
            current_sum+=num
        else:
            if current_length>max_length:
                max_length=current_length
                longest_sum=[current_sum]
            elif current_length==max_length:
                longest_sum.append(current_sum)
            current_length=0
            current_sum=0
    if current_length>max_length:
        max_length=current_length
        longest_sum=[current_sum]
    else:
        current_length==max_length
        longest_sum.append(current_sum)
    print(sum(longest_sum) if longest_sum else -1)
 
input1=[3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]   
(sum_of_odd(input1))

input1=[1,3,5,2,7,9,11,4,13,15,17]   
(sum_of_odd(input1))

input1=[1,3,5,7,9]   
(sum_of_odd(input1))

input1=[2,4,6,8]   
(sum_of_odd(input1))
input1=[2,4,6,7,9,11]   
(sum_of_odd(input1))
input1=[1,3,5,2,4]   
(sum_of_odd(input1))
input1=[7]   
(sum_of_odd(input1))


          
            
        
##sum of Power of digit:
def sumOfPowerOfDigits(input1):
    num_str = str(input1)
    total_sum = 0
    
    for i in range(len(num_str)):
        base = int(num_str[i])
        if i + 1 < len(num_str):
            exponent = int(num_str[i+1])
        else:
            exponent = 0
        total_sum +=base ** exponent
    return total_sum
test_number=582109
print(sumOfPowerOfDigits(test_number))

input1=50
print(sumOfPowerOfDigits(input1))
test_number=7
print(sumOfPowerOfDigits(test_number))
    
input1=204
print(sumOfPowerOfDigits(input1))
input1=1111
print(sumOfPowerOfDigits(input1))  
input1=987  
print(sumOfPowerOfDigits(input1))
input1=105
print(sumOfPowerOfDigits(input1))
input1=1000
print(sumOfPowerOfDigits(input1))
input1=98
print(sumOfPowerOfDigits(input1))



###sumofsumsofdigits:
    
def sumOfSumsOfDigits(input1):
    #input1=582109
    num_str=str(input1)
    total_sum = 0
    

    for i in range(len(num_str)):
        digits = num_str[i:]
        digit_sum = sum(int(digit) for digit in digits)
        total_sum += digit_sum
    return total_sum 
input1=582109
print(sumOfSumsOfDigits(input1))

input1=111
print(sumOfSumsOfDigits(input1))   

input1=0
print(sumOfSumsOfDigits(input1))    
input1=321
print(sumOfSumsOfDigits(input1))
input1=123
print(sumOfSumsOfDigits(input1))
input1=9876543210
print(sumOfSumsOfDigits(input1))


###Identify possible words:
def identifyPossibleWords(input1,input2):
    words=input2.split(":")
    
    valid_words=[]
    
    input1=input1.strip()
    words=[word.strip() for word in words]
    for word in words:
        if len(word)!=len(input1):
            continue
        is_match=True
        for c1,c2 in zip(input1,word):
            if c1 =="-":
                continue
        if c1.lower()!=c2.lower():
            is_match=False
            break
        if is_match:
            valid_words.append(word.upper())
    return ":".join(valid_words)
input1="fi_er"
input2="fever:filer:filter:fixer:fibre:fiber:offer:tailor"        

output=identifyPossibleWords(input1,input2)
print(output)

print(f"expected:FILER:FIXER:FIBER,Got:{output}")

input1="-----"
input2="apple:ample:angle:alien:alert:abcde:banana"
output=identifyPossibleWords(input1,input2)
print(output) 

input1="Te_t"
input2="test:TEXT:TeSt:tent:tEsting"
output=identifyPossibleWords(input1,input2)
print(output) 

input1="W_rd"
input2="card:hard:wardrobe" 
output=identifyPossibleWords(input1,input2)
print(output) 

input1=" c_t "
input2="cat:cut:cot:cute"
output=identifyPossibleWords(input1,inpu2)
print(output) 

input1="_a__a"
input2="karma:salsa:kappa:kanna"
output=identifyPossibleWords(input1,inpur2)
print(output) 

###another logic###
def identifyPossibleWords(input1,input2):
    possible_words=input2.split(":")
    matched_words=[]
    
    for word in possible_words:
        if len(word)==len(input1) and all(c1 == c2 or c1 =="_" for c1,c2 in zip(input1,word)):
            matched_words.append(word.upper())
    return ":".join(matched_words)   
     
input1="fi_er"
input2="fever:filer:filter:fixer:fibre:fiber:offer:tailor"
print(identifyPossibleWords(input1,input2))


####Splitting 
each string into 3 parts:####
s1="John"
s2="Johny"
s3="Janardhan"
lst=[s1,s2,s3]
 
first_parts=[]
middle_parts=[]
end_parts=[]


for word in lst:
   n=len(word)
   m=n//3

   if n % 3 == 1:
       first=word[:1]
       middle=word[1:n-1]
       end = word[n-1:]
       elif:*
       first=word[:2]
       middle=word[2:n-2]
       end = word[n-2:]
   else:
       first=word[:m]
       middle=word[m:2*m]
       end = word[2*m:]

first_parts.append(first)
middle_parts.append(middle)
end_parts.append(end)

output1=''.join(first_parts)
output2=''.join(middle_parts)
output3=''.join(end_parts).swapcase()

print(output1)
print(output2)
print(output3)

 # print(f"First: {''.join(first)}, Middle: {''.join(middle)}, End:{''.join(end)}")
        
       
with open('c:/10-python/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)    


with open('d:/10-python/pi_digits,txt') as file_object:
    content = file_object.read()
print(contents.rstrip())    


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
        