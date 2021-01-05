import random

library = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

def passwordGenerator(length, library):

	temporaryPool = ''
	while (len(temporaryPool) < length):
	    temporaryPool += library[random.randint(0, len(library ) - 1)]
    return temporaryPool
