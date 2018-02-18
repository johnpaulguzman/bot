import time
import threading
import sys

#from teleporter import Teleporter
from healer import Healer
#from attacker import Attacker
#from buffer import Buffer

#teleporter = Teleporter()
#thread_teleport = threading.Thread(name='thread-teleport', target=teleporter.run, daemon=True)

healer = Healer(None)
thread_heal = threading.Thread(name='thread-heal', target=healer.run, daemon=True)

#attacker = Attacker(teleporter)
#thread_attack = threading.Thread(name='thread-attack', target=attacker.run, daemon=True)

#buffer = Buffer()
#thread_buff = threading.Thread(name='thread-buff', target=buffer.run, daemon=True)


threads = [thread_heal]
# MEMORY LEAKING

from pympler import summary, muppy

if __name__ == '__main__':
    for thread in threads:
        thread.start()
    while True:
        all_objects = muppy.get_objects()
        sum1 = summary.summarize(all_objects)
        summary.print_(sum1)  
