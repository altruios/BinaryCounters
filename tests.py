import BinaryCounters as BC
from PIL import Image
import numpy as np
import os
import time
import math
C_UP= '\033[F'
base_dir = os.path.realpath(".") 
print("hello world");
bgcolors = [
    '\033[95m',
    '\033[94m',
    '\033[96m',
    '\033[92m',
    '\033[93m',
    '\033[91m',
    '\033[0m',
    '\033[1m',
    '\033[4m'
]


test1 = BC.BC(0,20)
test2 = BC.BC(0,20)
test3 = BC.BC(0,10)
test4 = BC.BC(0,10)
i=0
tests = []
while test1.VAL()<500:
     i=i+1
     test1.INCREASE(i)
     test2.INCREASE(1)
     test1.READ()
     test2.READ()
     test4.INCREASE(3)
     print("increases done\n\n")
     test3.INCREASE(i+1)
     test1.W_BIT_OP(test3,BC.AND)
     test1.READ()
     test3.READ()
     print("op done\n\n")
     test3.SORT_B(False)
     test3.READ()
     print("test3 sorted");
     test4.SORT_B(True)
     test4.SHIFT_CIRCLE_F(1)
     test4.READ()
     tests.append(test1.SPAWN(0,i%(test1._length()-1)))

for test in tests:
     print("\n test: \n")
     print(test.binary);