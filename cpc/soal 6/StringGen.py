import random
import string
from enum import Enum
class type(Enum):
    a="fire"
    b="water"
    c="electric"
    d="grass"
    e="stell"

def randomString():
    cde = "1234567890"
    return random.choice(list(type)).value+ " "+random.choice(list(type)).value+" "+''.join(random.choice(cde) for i in range(3)) +" "+''.join(random.choice(cde) for i in range(3))
for i in range(100):
    print (randomString())
