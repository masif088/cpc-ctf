import random
import string
from random import randrange


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = "0123456789"
    return int(''.join(random.choice(letters) for i in range(stringLength)))
print(100)
for i in range(100):
    print (str(randrange(255)) + ' ' +str(randrange(255)) + ' ' +str(randrange(255)))
