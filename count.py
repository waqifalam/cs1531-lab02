'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    char = {}
    for ch in text:
        if ch in char:
            char[ch] += 1
        else:
            char[ch] = 1
    for ch in char:
        print("{0} {1}".format(ch, char[ch]))

def count_char_insensitive(text):
    char = {}
    for ch in text:
        ch = ch.lower()
        if ch in char:
            char[ch] += 1
        else:
            char[ch] = 1
    for ch in char:
        print("{0} {1}".format(ch, char[ch]))

# bonus task:
def count_char_ordered(text):
    pass
    # add your code here 

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
count_char_ordered(text2)

