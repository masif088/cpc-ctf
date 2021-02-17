import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = "44555556666888999789"
    return int(''.join(random.choice(letters) for i in range(stringLength)))
def ran():
    """Generate a random string of fixed length """
    letters = "123456789"
    return int(''.join(random.choice(letters) for i in range(1)))
def rana():
    """Generate a random string of fixed length """
    letters = "123"
    return int(''.join(random.choice(letters) for i in range(1)))


print(100)
for i in range(100):
    a=ran()
    print(rana())
    print(a)
    for j in range(a):
        print (randomString(12))
