num1 = 42 #variable declaration, initialize number
num2 = 2.3 #variable declaration, initialize number
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuples
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #log statement, access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #add value
print(fruit[2]) #log statement

if num1 > 45:  #conditional if
    print("It's greater") #log statement 
else: #conditional else
    print("It's lower")   #log statement

if len(string) < 5: #conditional if
    print("It's a short word!")  #log statement 
elif len(string) > 15: #conditional elif
    print("It's a long word!")  #log statement
else: #conditional else
    print("Just right!")  #log statement

for x in range(5): #for loop up, stop, increment, sequence
    print(x)  #increment
for x in range(2,5): #for loop start, stop, increment, sequence
    print(x) #log statement
for x in range(2,10,3):  #for loop start, stop, increment, sequence
    print(x) #log statement
x = 0 #variable declaration, initialize number
while(x < 5): #while loop, start, stop
    print(x) #log statement
    x += 1 #increment 

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value

print(person) #log statement
person.pop('eye_color') #delete value
print(person) #log statement

for topping in pizza_toppings: #for loop, start, stop, increment, sequence 
    if topping == 'Pepperoni': #conditional if
        continue #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional if
        break #break

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop, stop, increment, sequence
        print('Hello') #log statement

print_hello_ten_times() #calling function

def print_hello_x_times(x): #function declaration, parameter
    for num in range(x): #for loop, stop, increment, sequence
        print('Hello') #log statement

print_hello_x_times(4) #calling function, argument 

def print_hello_x_or_ten_times(x = 10): #function declaration, parameter 
    for num in range(x): #for loop, stop, increment, sequence
        print('Hello') #log statement

print_hello_x_or_ten_times() #calling function
print_hello_x_or_ten_times(4) #calling function, argument 


"""
Bonus section #multiline comment
"""

# print(num3) NameError: name <variable name> is not defined 
# num3 = 72  variable declaration, initialize number
# fruit[0] = 'cranberry' typeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) KeyError: 'favorite_team'
# print(pizza_toppings[7]) IndexError: list index out of range
#   print(boolean)  IndentationError: unexpected indent
# fruit.append('raspberry') AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) AttributeError: 'tuple' object has no attribute 'pop'