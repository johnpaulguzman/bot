import time
import threading

from healer import Healer
from teleporter import Teleporter
from attacker import Attacker


healer = Healer()
teleporter = Teleporter()
attacker = Attacker(teleporter)

thread_heal = threading.Thread(name='thread-heal', target=healer.run, daemon=True)
thread_teleport = threading.Thread(name='thread-teleport', target=teleporter.run, daemon=True)
thread_attack = threading.Thread(name='thread-attack', target=attacker.run, daemon=True)
threads = [thread_heal, thread_teleport, thread_attack]

def run_threads():
    for thread in threads: thread.start()
    while True: pass

run_threads()