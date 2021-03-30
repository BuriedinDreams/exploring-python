print("hello world")

message = "storing stuff in a variable"

print(message)

price = 10
# just like javascript I have assigned the price to a new number 
price = 20
# price = 5.1 -- this is still called a float
is_published = False
print(price)

print("------------------------------")


patient_name = ("John Smith")
age = 20
is_new = True

name = input('What is your name? ')
print('Hi ' + name)

color = input('What is your Favorite color? ')
print('Hi ' + name + " your favorite color is " + color)


print("------------------------------")

birth_year = input('what is your Birth year?: ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
print(age)

course = "Python for 'Beginners' "

print(course)

x = -2.9

print(round(x)) # this will round the number to the nearest whole num
print(abs(x)) # this will turn a negative number positive or Absolute

print(abs(-55.7)) # I can also feed it a number Manually. 


print("------------------------------")

# IF Statements

is_hot = False # By changing this to False the statement underneath the if statement won't run because it's looking for a true.
is_cold = True # 

if is_hot:  # anything that we indent and is under an IF statement will run for the IF statement if statement is true.
  print("It's a hot a day") # If I change the boolean to False it will not run this
  print("Drink plenty of water")
elif is_cold: 
  print("It's a cold a day")
  print("Wear warm clothes")
else: # this will only run IF both of the statements are False
  print("It's a lovely day.")


print("------------------------------")
# FOR Loops 

# This will print out each letter of the word Python
# for item in 'Python':
#   print(item)

for item in ["Laptop","Phone","NoteBook","Pen"]:
  print(item)


# in the range function we can tell it where to start counting. - I used 5 and stop at 11, which, will print 10. We can also tell it to count by x numbers.
for num in range(5, 21, 2):
  print(num)

prices = [10, 20, 30]

total = 0
for price in prices:
  total = total + price
# print(total)
print(f"the total: {total} ") # the f stands for formatted string. This allows us add a variable inside of a string

print("------------------------------")

# Lists
names = [ "Zack", "Ben", "Mary", "Sarah", "Jake" ]

print(names) # this will print the whole list of names
print(names[2]) # this will print the index 2
print(names[2:4]) # this will print index 2 & 3. it won't print because that's when I told it to stop printing.
print(names[1:5]) # This will print all the names but mine - Zack



# I want to compare numbers from a list and see what is the largest number.
numbers = [2, 5, 9, 18, 21, 42, 3]

max = numbers[0] 

for number in numbers:
  if number > max:
    max = number
print (f"the largest number is: {max}")

print("------------------------------")

# functions

# to start a function you use def - "define"

def greet_friend(friends_name, favorite_color):
  print(f"Hi {friends_name} ")
  print(f"I didn't know your favorite color was {favorite_color}")

greet_friend("Sam","Green")

print("------------")

def add_numbers (num1, num2):
  return num1 + num2
  # print(f"Sum of {num1} and {num2}")


a = int(input("Enter a number you want to add: "))
b = int(input("Enter the other number you want to add: "))
c = add_numbers(a,b)

print(f"The Sum of {a} and {b} equal {c} ")



print("------------------------------")

