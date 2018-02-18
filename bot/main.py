import time
import threading
import sys

#from teleporter import Teleporter
from healer import Healer
#from attacker import Attacker
#from buffer import Buffer

#teleporter = Teleporter()
healer = Healer(None)
#attacker = Attacker(teleporter)
#buffer = Buffer()


threads = [
#    teleporter,
    healer,
#    attacker,
#    buffer,
]


from pympler import summary, muppy

if __name__ == '__main__':
    for thread in threads:
        thread.start()
    while True:
        all_objects = muppy.get_objects()
        sum1 = summary.summarize(all_objects)
        summary.print_(sum1)  
