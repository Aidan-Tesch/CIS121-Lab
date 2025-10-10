
#take string, return list with all words in said string

'''
def string_split(my_string):
    my_list = my_string.split()
    return my_list

def check_vowels(words):
    total_words = []
    for word in words:
        count = 0
        for letter in word:
                if letter in "aeiou":
                    count+=1
        if count >= 2:
            total_words.append(word)
    return total_words

word = "Peter Piper picked a peck of pickled pepprs."

words = string_split(word)

print(check_vowels(words))
'''
'''
#Define Dictonary
phonebook = {
    "Matt" : 5073891438,
    "Aidan" : 5073391652,
}
#Add to Dictonary
phonebook["Mother"] = 5075813400

#Look Up a Value
print(phonebook["Aidan"])

for person in phonebook:
    print(person, phonebook[person])
'''

my_word = "peter piper picked a peck of pickled peppers"

def letter_counter(word):
    letter_dictonary = {}
    for letter in word:
        if letter in letter_dictonary:
            letter_dictonary[letter] += 1
        else:
            letter_dictonary[letter] = 1
    return letter_dictonary

letter_dict = letter_counter(my_word)

for letter in letter_dict:
    print(letter, letter_dict[letter])

