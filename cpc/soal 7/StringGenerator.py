import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = "abcdefghijklmnopqrstuvwxyz "
    return (''.join(random.choice(letters) for i in range(stringLength)))
print("100")
for i in range(100):
    print (randomString(20))
