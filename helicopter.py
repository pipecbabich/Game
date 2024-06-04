from randfile import randcell
import os

class Helicopter():
    def __init__(self, w, h):
        rc = randcell(w,h)
        rw, rh = rc[0], rc[1]
        self.hw = rw
        self.hh = rh
        self.h = h
        self.w = w
        self.tank = 0
        self.mtank = 1
        self.score = 0
        self.lives = 30

    def moves(self, dw, dh):
        nw, nh = dw + self.hw, dh + self.hh
        if (nw >= 0 and nh >=0) and (nw < self.w and nh < self.h):
            self.hw, self.hh = nw, nh
            
    def stats_menu(self,):
        print('💧 ', self.tank, '/',self.mtank, sep='', end = ' | ')
        print('💰', self.score, end = " | ")
        print('❤️ ', int(self.lives))

    def export_data(self):
        return {'h': self.hh,
                'w': self.hw,
                'tank': self.tank,
                'mtank': self.mtank,
                'score': self.score,
                'lives': self.lives}
        
    def import_data(self, data):
        self.hh = data['h'] or 0
        self.hw = data['w'] or 0
        self.tank = data['tank'] or 0
        self.mtank = data['mtank'] or 1
        self.lives = data['lives'] or 30
        self.score = data['score'] or 0

        

        