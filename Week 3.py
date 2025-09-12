# Created by Aidan Tesch

# Question 1
# Assignment 1 : 5
# Assignment 2 : 3
# Assignment 3 : 2
# Assignment 4 : 12

# Question 2
# 1. Both if statements will run
# 2. Only one or the other will run

#Question 3
#light_color = input()
#if light_color == "red":
    #print("stop")
#elif light_color == "yellow":
    #print("yield")
#elif light_color == "green":
    #print("go")
#else:
    #print("invalid")

# Question 4
#age = int(input("Enter your age: "))
#goal = input("Enter your athleticism goal: ")
#if age >= 20 and age <= 39:
    #if goal == "Above Average":
        #print("Your resting heart rate should be between 47-72.")
    #elif goal == "Below Average":
        #print("Your resting heart rate should be between 73-93.")
    #else:
        #print("Error")
#elif age >= 40 and age <= 59:
    #if goal == "Above Average":
        #print("Your resting heart rate should be between 46-71.")
    #elif goal == "Below Average":
        #print("Your resting heart rate should be between 72-94.")
    #else:
        #print("Error")
#elif age >= 60 and age <= 79:
    #if goal == "Above Average":
        #print("Your resting heart rate should be between 45-70.")
    #elif goal == "Below Average":
        #print("Your resting heart rate should be between 71-97.")
    #else:
        #print("Error")


#Question 5
number_one = int(input("Pick a number: "))
number_two = int(input("Pick another number: "))
number_three = int(input("Pick another number: "))
my_list = [number_one, number_two, number_three]
if my_list[0] > my_list[1]:
    temp = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = temp
if my_list[1] > my_list[2]:
    temp = my_list[1]
    my_list[1] = my_list[2]
    my_list[2] = temp
for i in range(len(my_list)):
    print(my_list[i])
    
#Question 6
number_one = int(input("Pick a number: "))
number_two = int(input("Pick another number: "))
number_three = int(input("Pick another number: "))
my_list = [number_one, number_two, number_three]
if my_list[0] < my_list[1]:
    temp = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = temp
if my_list[1] < my_list[2]:
    temp = my_list[1]
    my_list[1] = my_list[2]
    my_list[2] = temp
for i in range(len(my_list)):
    print(my_list[i])










# Question 8
number_one = int(input("Pick a number: "))
number_two = int(input("Pick another number: "))
number_three = int(input("Pick another number: "))
largest_num = 0

if (number_one > number_two):
    largest_num = number_one
else:
    largest_num = number_two
if number_three > largest_num:
    largest_num = number_three
print(f'The largest number is: {largest_num}')

# Question 9
number_one = int(input("Pick a number: "))
number_two = int(input("Pick another number: "))
number_three = int(input("Pick another number: "))
smallest_num = 0

if (number_one < number_two):
    smallest_num = number_one
else:
    smallest_num = number_two
if number_three < smallest_num:
    smallest_num = number_three
print(f'The smallest number is: {smallest_num}')