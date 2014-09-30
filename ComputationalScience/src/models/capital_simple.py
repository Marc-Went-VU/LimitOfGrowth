import func as f
from const import _Const
        
CONST = _Const()
class Capital:
    def __init__(self):
        self = self
    def run_model(self, 
                  start_year = CONST.START_YEAR, 
                  year_range = CONST.YEAR_RANGE, 
                  year_step = CONST.YEAR_STEP_SIZE,
                  fioaa = CONST.FIOAA, 
                  nri = CONST.INITIAL.NRI, 
                  ici = CONST.INITIAL.ICI, 
                  sci = CONST.INITIAL.SCI):
        
        results = []
        results.append(self.simple_captial_model(current_year = start_year, 
                                                 fioaa = fioaa, 
                                                 nr = nri, 
                                                 ic = ici, 
                                                 sc = sci,
                                                 year_step = year_step,
                                                 nri = nri))
        
        for x in f.drange(start_year+1, start_year+year_range, year_step):
            last_result = results[-1]
            results.append(self.simple_captial_model(current_year = x, 
                                                     fioaa = fioaa, 
                                                     nr = last_result[CONST.CAPITAL.NR], 
                                                     ic = last_result[CONST.CAPITAL.IC], 
                                                     sc = last_result[CONST.CAPITAL.SC],
                                                     year_step = year_step,
                                                     nri = nri))
        return results
        
    def simple_captial_model(self,  
                             current_year, 
                             fioaa, 
                             nr, 
                             ic, 
                             sc,
                             year_step = CONST.YEAR_STEP_SIZE,
                             nri = CONST.INITIAL.NRI):
        a132 = 0.0053
        a61 = 1.67
        
        fcaor = f.f135(nr/nri)
        io = ic * (1 - fcaor) / 3
        fioas = f.f64(sc/(a61 * io))
        
        dIC = (0.57 - fioas - fioaa) * io - ic/14
        dSC = fioas * io - sc/20 
        dNR = -1 * a132 * io
        
        nr += (dNR * year_step)
        ic += (dIC * year_step)
        sc += (dSC * year_step)
        ret = [current_year]
        ret.insert(CONST.CAPITAL.NR, nr)
        ret.insert(CONST.CAPITAL.IC, ic)
        ret.insert(CONST.CAPITAL.SC, sc)
        return ret

