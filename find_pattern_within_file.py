import re


def search_text(searched_pattern, text_file):
    """This function is used to find a pattern with a file."""
    #  This next three lines of codes open, reads, and close the text file
    textfile = open(f'{text_file}', 'r')
    filetext = textfile.read()
    textfile.close()

    #  This text file is stored in a list by splitting it by lines
    list1 = filetext.split('\n')
    print(list1)

    #  This 'for' loop is used to go through each lines of text to search for the pattern
    i = 0
    for i, line in enumerate(list1, i):
        matches = re.finditer(searched_pattern, line)
        #   Within for every match, a 'for' loop is required to list each iteration
        for m in matches:
            print('Line %s: %02d-%02d: %s' % (i, m.start(), m.end(), m.group(0)))

