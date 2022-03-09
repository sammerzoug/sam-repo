import re
import json

import find_pattern_within_file
import create_file

#  'f' variable is to create an empty file called 'TEXT.txt'
f = open('TEXT.txt', 'w+')
#  'create_file module' has method 'file_creation' to write text within 'f'
create_file.file_creation()

#  'searched_pattern' is used to store a regex argument
#  searched_pattern = r'\s{0,}ip\s{1,}address'
searched_pattern = input(r'Enter a regex expression to match a pattern: ')
#  find_pattern_within_file.search_text(), function calls, finds, and returns user's input
find_pattern_within_file.search_text(searched_pattern, 'TEXT.txt')
