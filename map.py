from randfile import randcelltree
from randfile import randcell
from randfile import randmoves


CELL_TYPES = "🟩🏥🏬🌲🟦🔥💝"
TREE_BONUS = 100
PRICE_UPGRADE = 500
PRICE_MED = 1000

class Map:

    def __init__(self, w,h):
        self.w = w
        self.h = h
        self.cell = [[0 for i in range(w)] for q in range(h)]
        self.generate_forest(5,10)
        self.generate_river(20)
        self.generate_river(10)
        self.generate_shop()
        self.generate_med()
    
    def print_map(self, helico, clouds):
        print("⬛" * (self.w + 2))
        for mi in range(self.h):
            print("⬛", end = "")
            for mq in range(self.w):
                cell=self.cell[mi][mq]
                if (clouds.cell[mi][mq] == 1):
                    print("⚪", end="")
                elif (clouds.cell[mi][mq] == 2):
                    print("⚡", end="")
                elif (helico.hh == mi and helico.hw == mq):
                    print("🚁", end="")
                elif cell >= 0 and cell <= len(CELL_TYPES):
                    print(CELL_TYPES[cell], end = "")
            print("⬛")
        print("⬛" * (self.w + 2))

    def check_cell(self,x,y):
        if (x < 0 or y < 0) or (x >= (self.w-1) or y >= (self.h-1)):
            return False
        return True
    
    
    def generate_forest(self,r , mxr ):
        for ri in range(self.h):
            for ci in range(self.w):
                if randcelltree(r,mxr):
                    self.cell[ri][ci]=3
    def generate_river(self, l):
        rv1 = randcell(self.w,self.h) 
        rw, rh = rv1[0], rv1[1]
        self.cell[rh][rw] = 4
        while l > 0:
            mv = randmoves(rh,rw)
            rh1, rw1 = mv[0],mv[1]
            if self.check_cell(rw1,rh1):
                self.cell[rh1][rw1] = 4
                rh, rw = rh1, rw1
                l -= 1
    def generate_tree(self):
        tree=randcell(self.w, self.h)
        tw, th = tree[0], tree[1]
        if (self.cell[th][tw]==0):
            self.cell[th][tw] = 3

    def generate_fires(self):
        fires=randcell(self.w, self.h)
        fw, fh = fires[0],fires[1]
        if self.cell[fh][fw] == 3:
            self.cell[fh][fw] = 5
    def update_fire(self):
        for fi in range(self.h):
            for fq in range(self.w):
                cell = self.cell[fi][fq]
                if cell == 5:
                    self.cell[fi][fq] = 0
        for i in range(10):
            self.generate_fires() 
         

    def process_helicopter(self, helico, clouds):
        c = self.cell[helico.hh][helico.hw]
        d = clouds.cell[helico.hh][helico.hw]
        if c == 4:
            helico.tank = helico.mtank
        if c == 5 and helico.tank > 0:
            helico.tank -= 1
            self.cell[helico.hh][helico.hw] = 3
            helico.score += TREE_BONUS
        if c == 2 and helico.score >= PRICE_UPGRADE:
            helico.score -= PRICE_UPGRADE
            helico.mtank += 1

        if c == 1 and helico.score >= PRICE_MED:
            helico.lives += 10
            helico.score -= PRICE_MED
        
        if d == 2:
            helico.lives -= 0.1
            
            
    
    def generate_shop(self):
        rc=randcell(self.w, self.h)
        sw, sh = rc[0], rc[1]
        self.cell[sh][sw] = 2

    def generate_med(self):
        rc=randcell(self.w, self.h)
        sw, sh = rc[0], rc[1]
        if self.cell[sh][sw] != 2:
            self.cell[sh][sw] = 1
        else:
            self.generate_med()




