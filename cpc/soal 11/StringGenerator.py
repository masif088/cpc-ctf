import random
import string
from enum import Enum
def randomString():
    cde = "1234560"
    return str(int(''.join(random.choice(cde) for i in range(2))))
print(100)
for i in range(100):
    print (randomString())
