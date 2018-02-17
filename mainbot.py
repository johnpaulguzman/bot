import time
import threading

from teleporter import Teleporter
from healer import Healer
from attacker import Attacker


teleporter = Teleporter()
healer = Healer(teleporter)
attacker = Attacker(teleporter)

thread_teleport = threading.Thread(name='thread-teleport', target=teleporter.run, daemon=True)
thread_heal = threading.Thread(name='thread-heal', target=healer.run, daemon=True)
thread_attack = threading.Thread(name='thread-attack', target=attacker.run, daemon=True)
threads = [thread_teleport, thread_heal, thread_attack]

def run_threads():
    for thread in threads: thread.start()
    while True: pass

run_threads()