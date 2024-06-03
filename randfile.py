from random import randint as rand 

def randcelltree(r,mxr):
    t = rand(0,mxr)
    return (t <= r)

def randcell(w,h):
    rw = rand(0,w-1)
    rh = rand(0,h-1)
    return (rw,rh)

def randmoves(x,y):
    s=rand(0,3)
    moves = [(-1,0),(0,1),(1,0),(0,-1)]
    dx, dy = moves[s][0], moves [s][1]
    return (x + dx, y + dy)




