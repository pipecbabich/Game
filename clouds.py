from randfile import randcelltree as randcellclo


class Clouds():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cell = [[0 for i in range(w)] for q in range(h)] 

    def update_clouds(self, r=1, mxr=20, gr=1, mxgr=10):
        for ri in range(self.h):
            for ci in range(self.w):
                if randcellclo(r,mxr):
                    self.cell[ri][ci]=1
                    
                    if randcellclo(gr,mxgr):
                        self.cell[ri][ci]=2
                else:
                    self.cell[ri][ci]=0 

    def export_data(self):
        return {'cell': self.cell}     
    def import_data(self, data):
        self.cell = data['cell'] or [[0 for i in range(self.w)] for q in range(self.h)]  
                    
                        

    