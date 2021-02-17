import random
import string
from enum import Enum

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    abc = "ABCDEFGH"
    cde = "12345678"
    return ''.join(random.choice(abc) for i in range(1))+''.join(random.choice(cde) for i in range(1))+ " "+''.join(random.choice(abc) for i in range(1))+''.join(random.choice(cde) for i in range(1))
for i in range(100):
    print (randomString(4))
