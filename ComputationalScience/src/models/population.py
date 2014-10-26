import func as f
from const import _Const
        
CONST = _Const()
class Population:
    def __init__(self, start_year):
        self = self
        self.start_year = start_year
        self.POP    = CONST.INITIAL.POPI
        self.EHSPC  = CONST.INITIAL.EHSPCI
        self.AIOPC  = CONST.INITIAL.AIOPCI
        self.DIOPC  = CONST.INITIAL.DIOPCI
        self.FCFPC  = CONST.INITIAL.FCFPCI
        self.PLE    = CONST.INITIAL.PLEI
        
        self.delayedDIOPCold={}
        self.delayedFCFPCold={}
        self.delayedPLEold={}
        self.delayedDIOPCnew={}
        self.delayedFCFPCnew={}
        self.delayedPLEnew={}
        
    def initial_result(self):
        ret = {}
        ret[CONST.RETURNS.POP] = CONST.INITIAL.POPI
        return ret 
    
    def model(self, current_year,
                  io, so, F, ppolx,
                  year_step= CONST.YEAR_STEP_SIZE
                  ):        
        #Calculation of Death rate
        FPC = F/self.POP
        SOPC = so/self.POP
        HSAPC = f.f21(SOPC)
        IOPC = io/self.POP
        LMC = 1 - (f.f27(IOPC)* f.f26(self.POP))
        LE = 28. * f.f25(self.EHSPC) * f.f20(FPC/230) * f.f29(ppolx) * LMC
        D = self.POP/LE

        #Calculation of Birth rate
        FIE = (IOPC - self.AIOPC)/self.AIOPC
        DCFS = 4*f.f41(FIE)*f.f39(self.DIOPC)
        DTF = DCFS*f.f36(self.PLE)
        MTF = 12*f.f34(LE)
        FCAPC = SOPC * f.f48(MTF/DTF - 1)                
        FCE = f.f45(self.FCFPC)
        TF = min(MTF, MTF * (1 - FCE) + (DTF * FCE))
        B = 0.21 * self.POP * TF/30
                
        dPOP = B - D
        dEHSPC = (HSAPC - self.EHSPC)/20
        dAIOPC = (IOPC - self.AIOPC)/3
        
        if len(self.delayedDIOPCold) == 0:
            self.delayedDIOPCnew = {1: IOPC, 2: IOPC, 3: IOPC}
        else:
            delayPerStage = 20/3
            
            self.delayedDIOPCnew[1] = self.delayedDIOPCold[1] + year_step * (IOPC - self.delayedDIOPCold[1])                    / delayPerStage;
            self.delayedDIOPCnew[2] = self.delayedDIOPCold[2] + year_step * (self.delayedDIOPCold[1] - self.delayedDIOPCold[2]) / delayPerStage;
            self.delayedDIOPCnew[3] = self.delayedDIOPCold[3] + year_step * (self.delayedDIOPCold[2] - self.delayedDIOPCold[3]) / delayPerStage;

        self.delayedDIOPCold = self.delayedDIOPCnew        
 
        if len(self.delayedFCFPCold) == 0:
            self.delayedFCFPCnew = {1: FCAPC, 2: FCAPC, 3: FCAPC}
        else:
            delayPerStage = 20/3
            
            self.delayedFCFPCnew[1] = self.delayedFCFPCold[1] + year_step * (FCAPC - self.delayedFCFPCold[1])                    / delayPerStage;
            self.delayedFCFPCnew[2] = self.delayedFCFPCold[2] + year_step * (self.delayedFCFPCold[1] - self.delayedFCFPCold[2]) / delayPerStage;
            self.delayedFCFPCnew[3] = self.delayedFCFPCold[3] + year_step * (self.delayedFCFPCold[2] - self.delayedFCFPCold[3]) / delayPerStage;

        self.delayedFCFPCold = self.delayedFCFPCnew
        
        if len(self.delayedPLEold) == 0:
            self.delayedPLEnew = {1: LE, 2: LE, 3: LE}
        else:
            delayPerStage = 20/3
            
            self.delayedPLEnew[1] = self.delayedPLEold[1] + year_step * (LE - self.delayedPLEold[1])                    / delayPerStage;
            self.delayedPLEnew[2] = self.delayedPLEold[2] + year_step * (self.delayedPLEold[1] - self.delayedPLEold[2]) / delayPerStage;
            self.delayedPLEnew[3] = self.delayedPLEold[3] + year_step * (self.delayedPLEold[2] - self.delayedPLEold[3]) / delayPerStage;

        self.delayedPLEold = self.delayedPLEnew
        
        dDIOPC = self.delayedDIOPCnew[3]
        dFCFPC = self.delayedFCFPCnew[3]
        dPLE = self.delayedPLEnew[3]
        
        self.POP    += (dPOP * year_step)
        self.EHSPC  += (dEHSPC * year_step)
        self.AIOPC  += (dAIOPC * year_step)
        self.DIOPC  += (dDIOPC * year_step)
        self.FCFPC  += (dFCFPC * year_step)
        self.PLE    += (dPLE * year_step)
        
        ret = {}
        ret[CONST.RETURNS.POP] = self.POP
        return ret