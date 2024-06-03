from randfile import randcell


class Helicopter():
    def __init__(self, w, h):
        rc = randcell(w,h)
        rw, rh = rc[0], rc[1]
        self.hw = rw
        self.hh = rh
        self.h = h
        self.w = w

    def moves(self, dw, dh):
        nw, nh = dw + self.hw, dh + self.hh
        if (nw >= 0 and nh >=0) and (nw < self.w and nh < self.h):
            self.hw, self.hh = nw, nh
            


#helico = Helicopter(20,10)
#print(helico.hh,helico.hw)
#helico.moves(0,1)
#print(helico.hh,helico.hw)
        

        