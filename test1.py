#Printing in Python

print("Hello World!!")

#Variables in python

test_string = "This is a test string"
name = "Priyank"
value = 2
decimal_value = 2.0
bool_value = True

#printing using variables

print(f"This is a test string from {name}".lower())
print(f"The value of decimal is: {decimal_value} and bool_value: {bool_value}".upper())

#array and iteration over array
array_of_numbers = [1,2,3,4,5,6,7,8,9,0]

total_of_array = 0
for value in array_of_numbers:
    total_of_array += value

print(total_of_array)

#Taking user input

your_name = input("Enter your name: ")

print(f"welcome {your_name}")

#Defining a function in Python
def sum_of_two_numbers(num1, num2=2):
    return num1 + num2

num1 = int(input("Enter a number to Add "))
num2 = int(input("Enter a number to add "))
total = sum_of_two_numbers(num1, num2)
print(f"Total of {num1} + {num2} = {total}")


#Python Dictionary
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

print(cities['CA'])
print(cities['MI'])
