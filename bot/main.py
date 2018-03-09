import os
import sys
import time
import threading

import constants
from kafra import Kafra
from teleporter import Teleporter
from healer import Healer
from attacker import Attacker
from buffer import Buffer
from notifier import Notifier
from kswarn import KSWarn


def execute_memory_leak_hack_in(secs=1):
    print("Restarting in {} seconds".format(secs))
    time.sleep(secs)
    print("Executing a restart...")
    os.execl(sys.executable, sys.executable, *sys.argv) 

kafra = Kafra()
teleporter = Teleporter()
healer = Healer(teleporter)
attacker = Attacker(teleporter, execute_memory_leak_hack_in)
buffer = Buffer(teleporter)
notifier = Notifier(execute_memory_leak_hack_in)
kswarn = KSWarn(teleporter)

threads = [
    teleporter,
    #healer,
    attacker,
    #buffer,
    #notifier,
    #kswarn,
]

#import psutil 
#pid = os.getpid() 
#py = psutil.Process(pid)
#memoryUse = py.memory_info()[0]/2.**30 # memory use in GB...I think 
#print('memory use:', memoryUse)

if __name__ == '__main__':
    kafra.run()
    for thread in threads: thread.start()
    execute_memory_leak_hack_in(constants.Constants.kill_time)
