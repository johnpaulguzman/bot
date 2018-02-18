import os
import sys
import time
import threading

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

pympler_prints = 0
restart_timer = 180

def execute_memory_leak_hack_in(secs):
    time.sleep(secs)
    os.execl(sys.executable, sys.executable, *sys.argv) 

from pympler import summary, muppy

if __name__ == '__main__':
    for thread in threads: thread.start()
    for i in range(pympler_prints):
        all_objects = muppy.get_objects()
        sum1 = summary.summarize(all_objects)
        summary.print_(sum1)
    execute_memory_leak_hack_in(restart_timer)
