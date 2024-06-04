from pynput import keyboard
from map import Map
import time
import os
from helicopter import Helicopter
from clouds import Clouds

TICK_SLEEP = 0.005
TICK_TREE = 500
TICK_FIRE = 500
TICK_CLOUDS = 250
MAP_W, MAP_H = 20, 10
MOVES = {'w':(-1,0),'a':(0,-1),'s':(1,0), 'd': (0,1)}

field=Map(MAP_W, MAP_H)

clouds=Clouds(MAP_W, MAP_H)

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
    helico.stats_menu()
    field.process_helicopter(helico, clouds)
    field.print_map(helico, clouds)
    tick += 1
    if (tick % TICK_TREE == 0):
        field.generate_tree()
    if (tick % TICK_FIRE == 0):
        field.update_fire()
    if (tick % TICK_CLOUDS == 0):
        clouds.update_clouds()
    print("TICK", tick)
    time.sleep(TICK_SLEEP)
    

