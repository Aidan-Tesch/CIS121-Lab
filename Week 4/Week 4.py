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
# Question 2
user_word = input("Enter any word: ")
for i in range(1,len(user_word),2):
        print(user_word[i], end="")

# Question 3
'''
for i in range(37, 1051):
    if i % 2 == 0:
        print(i)
'''

# Question 44
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




