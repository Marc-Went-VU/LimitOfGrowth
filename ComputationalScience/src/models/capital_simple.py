import func as f
from const import _Const
        
CONST = _Const()
class Capital:
    def __init__(self, start_year):
        self = self
        self.start_year = start_year
        
        self.NR = CONST.INITIAL.NRI
        self.IC = CONST.INITIAL.ICI
        self.SC = CONST.INITIAL.NRI
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
    def initial_result(self):
        ret = {}
        ret[CONST.RETURNS.IO] = CONST.INITIAL.IOI
        
        ret[CONST.RETURNS.IC] = CONST.INITIAL.ICI
        ret[CONST.RETURNS.NR] = CONST.INITIAL.NRI
        ret[CONST.RETURNS.SC] = CONST.INITIAL.SCI
        return ret    
    def model(self,  
                             current_year, 
                             fioaa, 
                             year_step = CONST.YEAR_STEP_SIZE):
        a132 = 0.0053
        a61 = 1.67
        
        fcaor = f.f135(self.NR / CONST.INITIAL.NRI)
        io = self.IC * (1 - fcaor) / 3
        fioas = f.f64(self.SC/(a61 * io))
        
        dIC = (0.57 - fioas - fioaa) * io - self.IC/14
        dSC = fioas * io - self.SC/20 
        dNR = -1 * a132 * io
        
        self.NR += (dNR * year_step)
        self.IC += (dIC * year_step)
        self.SC += (dSC * year_step)
        ret = {}
        ret[CONST.RETURNS.IO] = io
        
        ret[CONST.RETURNS.IC] = self.IC
        ret[CONST.RETURNS.NR] = self.NR
        ret[CONST.RETURNS.SC] = self.SC
        return ret

