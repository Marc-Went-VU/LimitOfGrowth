import func as f
from const import _Const
        
CONST = _Const()
class Pollution:
    def __init__(self, start_year):
        self = self
        self.start_year = start_year
        self.PPOL = CONST.INITIAL.PPOLI
        self.PPAPR = CONST.INITIAL.PPGRI
        
        self.delayedPPARPnew = {}
        self.delayedPPARPold = {}
 
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
        
        if len(self.delayedPPARPold) == 0:
            self.delayedPPARPnew = {1: PPGR, 2: PPGR, 3: PPGR}
        else:
            delayPerStage = 20/3
            
            self.delayedPPARPnew[1] = self.delayedPPARPold[1] + year_step * (PPGR - self.delayedPPARPold[1])                    / delayPerStage;
            self.delayedPPARPnew[2] = self.delayedPPARPold[2] + year_step * (self.delayedPPARPold[1] - self.delayedPPARPold[2]) / delayPerStage;
            self.delayedPPARPnew[3] = self.delayedPPARPold[3] + year_step * (self.delayedPPARPold[2] - self.delayedPPARPold[3]) / delayPerStage;

        self.delayedPPARPold = self.delayedPPARPnew
        
        dPPOL = self.PPAPR - PPASR
        dPPAPR = self.delayedPPARPnew[3]
        
        self.PPOL += (dPPOL * year_step)
        self.PPAPR += (dPPAPR * year_step)
                
        ret = {}
        ret[CONST.RETURNS.PPOLX] = PPOLX
        return ret
