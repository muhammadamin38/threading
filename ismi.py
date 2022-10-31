import threading
import time


from ism1 import *
from sh import *
from familya import *


t1 = threading.Thread(target=ism1)
t2 = threading.Thread(target=familya2)
t3 = threading.Thread(target=ism2)



t1.start()
t2.start()
t3.start()