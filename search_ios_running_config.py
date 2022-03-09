import re
import json

import find_pattern_within_file

#  'f' variable is to create an empty file called 'TEXT.txt'
f = open('TEXT.txt', 'w+')

while True:
    #  'g' variable is to open and append to the file called 'TEXT.txt'
    #  'x' is to collect user input
    g = open('TEXT.txt', 'a')
    x = input('Enter \"q\" to quit or "c" to continue: ')
    if x == 'q':
        g.close()
        break
    else:
        #  g.write('\n')
        g.write(input('Search "IOS" start-up configuration: '))
        g.write('\n')

#  'searched_pattern' is used to store a regex argument
#  searched_pattern = r'\s{0,}ip\s{1,}address'
searched_pattern = input(r'Enter a regex expression to match a pattern: ')
#  find_pattern_within_file.search_text(), function calls, finds, and returns user's input
find_pattern_within_file.search_text(searched_pattern, 'TEXT.txt')
