# Question 1
biggest = int(input("Enter the largest number: "))
smallest = int(input("Enter the smallest number: "))
count = 0
while biggest/2 > smallest:
    biggest /= 2
    count+=1
print(f'The Biggest number was divided {count} times.')

# Question 2
user_word = input("Enter any word: ")
for i in range(len(user_word)):
    if not(i % 2 == 0):
        print(user_word[i], end="")