import random

#part a 
#get a random number then round it to the number the user inputs

a = random.uniform(1, 100)
b = int(input("Give me a number:  "))
a = round(a, b)

print(a)

#part b
#ask for name and determine how many leters are in the name then output as an ID

firstName = str(input("What is your first name:  "))
lastName = str(input("What is your last name:  "))
def count_letters(firstName):
  count = 0
  for x in firstName:
    count += 1
  return str(count)
print("You're ID number is " + count_letters(firstName) + count_letters(lastName))
