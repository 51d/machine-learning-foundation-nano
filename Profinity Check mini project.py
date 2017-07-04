import urllib

def read_text():
    quotes = open(r'C:\files') #file destination whose we wish to check
    contents_of_file = quotes.read()
    quotes.close()
    check_profinity(contents_of_file)

def check_profinity(to_check):
    connection =  urllib.urlopen('http://wdyl.com/profinity?q=' + to_check)
    output = connection.read()
    connection.close()
    if 'true' in output:
        print 'check for bad words'
    elif 'false' in output:
        print 'good doc'
    else:
        print 'check coundnt occur'
