import time
import threading
import sys

from teleporter import Teleporter
from healer import Healer
from attacker import Attacker
from buffer import Buffer

teleporter = Teleporter()
healer = Healer(teleporter)
attacker = Attacker(teleporter)
buffer = Buffer()

thread_teleport = threading.Thread(name='thread-teleport', target=teleporter.run, daemon=True)
thread_heal = threading.Thread(name='thread-heal', target=healer.run, daemon=True)
thread_attack = threading.Thread(name='thread-attack', target=attacker.run, daemon=True)
thread_buff = threading.Thread(name='thread-buff', target=buffer.run, daemon=True)
threads = [thread_teleport, thread_heal, thread_attack, thread_buff]
## MEMORY LEAK ^^^

import os
import psutil
pid = os.getpid()
py = psutil.Process(pid)

if __name__ == '__main__':
    for thread in threads:
        thread.start()
    while True:
        memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
        print('memory use:', memoryUse)
