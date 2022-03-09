def file_creation():
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