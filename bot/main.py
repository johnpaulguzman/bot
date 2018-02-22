import os
import sys
import time
import threading

from constants import Constants
from teleporter import Teleporter
from healer import Healer
from attacker import Attacker
from buffer import Buffer
from notifier import Notifier

teleporter = Teleporter()
healer = Healer(teleporter)
attacker = Attacker(teleporter)
buffer = Buffer()
notifier = Notifier()

threads = [
    teleporter,
    healer,
    attacker,
#    buffer,
    notifier,
]

#import psutil 
#pid = os.getpid() 
#py = psutil.Process(pid)
#memoryUse = py.memory_info()[0]/2.**30 # memory use in GB...I think 
#print('memory use:', memoryUse)

def execute_memory_leak_hack_in(secs):
    print("Restarting in {} seconds".format(secs))
    time.sleep(secs)
    print("Executing a restart...")
    os.execl(sys.executable, sys.executable, *sys.argv) 

if __name__ == '__main__':
    for thread in threads: thread.start()
    execute_memory_leak_hack_in(Constants.teleport_time)
        
