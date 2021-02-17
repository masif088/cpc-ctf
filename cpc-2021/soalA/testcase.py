import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = "0123456789"
    return int(''.join(random.choice(letters) for i in range(stringLength)))
cde="0123456789"
print(100)
for i in range(100):
    print (str(int(''.join(random.choice(cde) for i in range(3))))+" "+str(int(''.join(random.choice(cde) for i in range(3)))))
