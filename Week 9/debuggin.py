def convert_knuts(knuts=900):
    knuts_per_sickle = 29
    sickles_per_galleon = 17
    knuts_per_galleon = knuts_per_sickle * sickles_per_galleon

    galleons = knuts // knuts_per_galleon
    remaining_knuts = knuts % knuts_per_galleon

    sickles = remaining_knuts // knuts_per_sickle
    remaining_knuts = remaining_knuts % knuts_per_sickle

    output = ""

    if galleons > 0:
        if galleons > 1:
            output = output + str(galleons) + " galleons "
        else:
            output = output + str(galleons) + " galleon "
    if sickles > 0:
        if sickles > 1:
            output = output + str(sickles) + " sickles "
        else:
            output = output + str(sickles) + " sickle "
    if remaining_knuts > 0:
        if remaining_knuts > 1:
            output = output + str(remaining_knuts) + " knuts"
        else:
            output = output + str(remaining_knuts) + " knut"
    return output

'''
print(convert_knuts(32))
print(convert_knuts())
print(convert_knuts(544))
print(convert_knuts(993))
'''

def highway_directions(highway_num):
    if 1 <= highway_num <= 99:
        if highway_num % 2 == 0:
            return f"I-{highway_num} runs east/west"
        else:
            return f"I-{highway_num} runs north/south"
    elif 100 <= highway_num <= 999:
        service_highway = highway_num % 100

        if 1 <= service_highway <= 99:
            if service_highway % 2 == 0:
                return f"I-{highway_num} runs east/west"
            elif service_highway % 2 != 0:
                return f"I-{highway_num} runs north/south"
        else:
            return f"I-{highway_num} is an invalid highway number"
    else:
        return f"I-{highway_num} is an invalid highway number"

'''
print(highway_directions(5))
print(highway_directions(82))
print(highway_directions(200))
print(highway_directions(353))
'''

def design_rug(width, length, pattern):
	result = "Your rug is:\n"
	for i in range(length):
		result += pattern * width
		if i < length - 1:
			result += "\n"
	return result

'''
print(design_rug(3,5,"$"))
print(design_rug(16,5,"@"))
'''

def count_duplicates(num_1, num_2, num_3):
	count = 0
	
	if num_1 == num_2:
		count += 1
	
	if num_1 == num_3:
		count += 1
          
	if num_2 == num_3:
		count += 1
	
	if count == 0:
		return "Each number is unique"
	elif count == 3:
		return "You entered the same number 3 times"
	else:
		return "You entered the same number 2 times"

'''
print(count_duplicates(2, 3, 2))
print(count_duplicates(4, 4, 4))
print(count_duplicates(1, 2, 3))
'''

def flip_flop(word):
	length = len(word)
	middle = length // 2

	if length % 2 == 0:
		first_half = word[:middle]
		second_half = word[middle:]
		return second_half + first_half
	else:
		first_part = word[:middle]
		middle_char = word[middle]
		last_part = word[middle+1:]
		return last_part + middle_char + first_part

'''
print(flip_flop("abcd"))
print(flip_flop("grapes"))
print(flip_flop("abcde"))
print(flip_flop("cranberries"))
'''

def hamming_distance(str1, str2):
	if len(str1) != len(str2):
		return "Strings must be of equal length."
	
	distance = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			distance += 1
	return distance

'''
print(hamming_distance("river", "rover"))
print(hamming_distance("cat", "dog"))
print(hamming_distance("cat", "hat"))
print(hamming_distance("cat", "banana"))
'''

def hailstone_seq(n):
	sequence = [n]
	
	while n != 1:
		if n % 2 == 0:
			n = n // 2
			sequence.append(n)
		else:
			n = 3 * n + 1
			sequence.append(n)
	return sequence
'''
print(hailstone_seq(25))
print(hailstone_seq(40))
'''

def like_or_dislike(events):
	state = "nothing"
	
	for event in events:
		if event == state:
			state = "nothing"
		else:
			state = event
	
	return state
'''
print(like_or_dislike(["dislike"]))
print(like_or_dislike(["like", "like"]))
print(like_or_dislike(["dislike", "like"]))
print(like_or_dislike(["like", "dislike", "dislike"]))
'''


def return_unique(numbers):
	number_dicitonary = {}
	#load dictionary
	for number in numbers:
		if number in number_dicitonary:
			number_dicitonary[number] += 1			
		else:
			number_dicitonary[number] = 1

	unique_numbers = []
	#find unique numbers in dictionary
	for number in number_dicitonary:
		if number_dicitonary[number] == 1:
			unique_numbers.append(number)
	return unique_numbers
'''
print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
'''

def find_factors(num):
	factors = []
	
	for i in range(1, num+1):
		if num % i == 0:
			factors.append(i)

	return factors
'''
print(find_factors(12))
print(find_factors(17))
print(find_factors(36))
'''

def palindromes(words):
    result = {"palindrome": [], "non-palindrome": []}
    for word in words:
        reversed_word = word[::-1]
        if reversed_word != word:
            result["non-palindrome"].append(word)
        else:
            result["palindrome"].append(word)
    return result
'''
print(palindromes(["madam", "racecar", "hello", "level", "python"]))
print(palindromes(["noon", "civic", "deed", "open", "loop"]))
print(palindromes(["apple", "banana", "cherry"]))
'''

from random import randint

def guess(guess="even"):
	value = randint(0, 9)
	
	if value % 2 == 0:
		actual = "even"
	else:
		actual = "odd"
	
	if guess == actual:
		return "Correct!"
	else:
		return "Incorrect!"
'''	
print(guess())
print(guess("odd"))
'''