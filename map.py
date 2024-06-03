from randfile import randcelltree
from randfile import randcell
from randfile import randmoves

CELL_TYPES = "🟩🏥🏬🌲🟦🔥"

class Map:

    def __init__(self, w,h):
        self.w = w
        self.h = h
        self.cell = [[0 for i in range(w)] for q in range(h)]

    def print_map(self, helico):
        print("⬛" * (self.w + 2))
        for mi in range(self.h):
            print("⬛", end = "")
            for mq in range(self.w):
                cell=self.cell[mi][mq]
                if (helico.hh == mi and helico.hw == mq):
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
         



