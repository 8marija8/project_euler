"""

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""

import os

cwd = os.getcwd()
file_path = os.path.join(cwd, 'problem_42', 'p042_words.txt')

triangle_numbers = [int((number/2)*(number+1)) for number in range(1,1000)]

total = 0

with open(file_path, 'r') as file:
    for line in file:
        words = line.strip().split(',')

        for word in words:
            
            word = word[1:-1]
            word_value = 0

            for letter in word:
                word_value += ord(letter)-64
            
            if word_value in triangle_numbers:
                total += 1

print("total:", total)