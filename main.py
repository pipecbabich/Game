from pynput import keyboard
from map import Map
import time
import os
from helicopter import Helicopter

TICK_SLEEP = 0.005
TICK_TREE = 500
TICK_FIRE = 500
MAP_W, MAP_H = 20, 10
MOVES = {'w':(-1,0),'a':(0,-1),'s':(1,0), 'd': (0,1)}

tmp=Map(MAP_W, MAP_H)
tmp.generate_forest(5,10)
tmp.generate_river(20)
tmp.generate_river(10)

helico = Helicopter(MAP_W, MAP_H)

def pro_key(key):
    global helico
    k = key.char.lower()
    if k == 'w' or k == 'a' or k=='s' or k=='d':
        #print(k)
        dh, dw = MOVES[k][0], MOVES[k][1]
        #print(dh, dw)
        helico.moves(dw,dh)
        #print(helico.hh,helico.hw)

listener = keyboard.Listener(
    on_press=None,
    on_release=pro_key)
listener.start()


tick = 1
while True:
    os.system('cls')
    print("TICK", tick)
    tmp.print_map(helico)
    tick += 1
    if (tick % TICK_TREE == 0):
        tmp.generate_tree()
    if (tick % TICK_FIRE == 0):
        tmp.update_fire()
    time.sleep(TICK_SLEEP)
    

