import os
import sys
import time
import threading

import constants
from teleporter import Teleporter
from healer import Healer
from attacker import Attacker
from buffer import Buffer

teleporter = Teleporter()
healer = Healer(teleporter)
attacker = Attacker(teleporter)
buffer = Buffer()

threads = [
    teleporter,
    healer,
    attacker,
#    buffer,
]

i_am_going_to_hell_for_this_sec = 180
import os 
import psutil 
pid = os.getpid() 
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30 # memory use in GB...I think 
print('memory use:', memoryUse) 

def execute_memory_leak_hack_in(secs):
    time.sleep(secs)
    os.execl(sys.executable, sys.executable, *sys.argv) 

if __name__ == '__main__':
    for thread in threads: thread.start()
    execute_memory_leak_hack_in(i_am_going_to_hell_for_this_sec)
        
