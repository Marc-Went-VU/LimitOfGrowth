import func as f
from const import _Const
        
CONST = _Const()
class Pollution:
    def __init__(self, start_year):
        self = self
        self.start_year = start_year
        self.PPOL = CONST.INITIAL.PPOLI
        self.PPAPR = CONST.INITIAL.PPGRI
        
        self.delaydPPAPR = {self.start_year: CONST.INITIAL.PPGRI}
 
    def initial_result(self):
        ret = {}
        ret[CONST.RETURNS.PPOLX] = CONST.INITIAL.PPOLXI
        return ret 
           
    def model(self, current_year,
                  io, pop, falm, ai,
                  year_step= CONST.YEAR_STEP_SIZE
                  ):        
        
        PPGAO = 0.001 * ai * (1 - falm)
        PPGIO = 0.02 * pop * f.f132(io/pop)
        PPGR = PPGIO + PPGAO
        PPOLX = self.PPOL/(1.36*10**8)
        AHL = 1.5 * f.f145(PPOLX)
        PPASR = self.PPOL/(1.4 * AHL)
        
        self.delaydPPAPR[current_year + 20/year_step] = PPGR
        
        dPPOL = self.PPAPR - PPASR
        dPPAPR = f.get_unprecise_index(self.delaydPPAPR, current_year)
        
        self.PPOL += (dPPOL * year_step)
        self.PPAPR += (dPPAPR * year_step)
        
        
        ret = {}
        ret[CONST.RETURNS.PPOLX] = PPOLX
        return ret
