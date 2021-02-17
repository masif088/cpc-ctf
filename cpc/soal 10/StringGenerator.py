import random
import string
from enum import Enum
def randomString():
    cde = "1234567890"
    return str(int(''.join(random.choice(cde) for i in range(3)))) +" "+str(float(''.join("0."+random.choice(cde) for i in range(1))))+" "+str(int(''.join(random.choice(cde) for i in range(2))))
print(100)
for i in range(100):
    print (randomString())
