import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = "0123456789"
    return int(''.join(random.choice(letters) for i in range(stringLength)))
for i in range(100):
    print (randomString(3))
