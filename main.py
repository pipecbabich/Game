from pynput import keyboard
from map import Map
import time
import os
from helicopter import Helicopter
from clouds import Clouds
import json

TICK_SLEEP = 0.005
TICK_TREE = 250
TICK_FIRE = 500
TICK_CLOUDS = 500
MAP_W, MAP_H = 20, 10
MOVES = {'w':(-1,0),'a':(0,-1),'s':(1,0), 'd': (0,1)}

field=Map(MAP_W, MAP_H)
clouds=Clouds(MAP_W, MAP_H)
helico = Helicopter(MAP_W, MAP_H)

def pro_key(key):
    global helico, field, clouds, tick
    k = key.char.lower()
    if k == 'w' or k == 'a' or k=='s' or k=='d':
        dh, dw = MOVES[k][0], MOVES[k][1]
        helico.moves(dw,dh)
    if k == 't':
        data = {'helicopter': helico.export_data(),
                'field': field.export_data(),
                'clouds': clouds.export_data(),
                'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    if k == 'r':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.import_data(data['helicopter'])
            field.import_data(data['field'])
            clouds.import_data(data['clouds'])

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
    
    

