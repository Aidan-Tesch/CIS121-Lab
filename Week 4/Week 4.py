# Question 1
'''
biggest = int(input("Enter the largest number: "))
smallest = int(input("Enter the smallest number: "))
count = 0
while biggest/2 > smallest:
    biggest /= 2
    count+=1
print(f'The Biggest number was divided {count} times.')
'''

'''
# Question 2
user_word = input("Enter any word: ")
for i in range(1,len(user_word),2):
        print(user_word[i], end="")
'''

# Question 3
'''
for i in range(37, 1051):
    if i % 2 == 0:
        print(i)
'''

# Question 4
'''
user_input = ""
final_string = ""
my_list = []
while user_input != "done":
    user_input = input("Enter a letter (or type done): ")
    if user_input != "done":
        my_list.append(user_input)
for i in range(len(my_list)):
    final_string = final_string + my_list[i]
print(final_string)
'''

# Question 5
'''
sum = 0
for i in range(51, 518, 2):
    sum += i
print(sum)
'''

# Question 6
user_input = 0
sum = 0
while user_input >= 0:
    user_input = int(input("Enter an integer: "))
    if user_input >= 0:
        sum += user_input
print(sum)


