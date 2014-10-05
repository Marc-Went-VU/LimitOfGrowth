import func as f
from const import _Const
        
CONST = _Const()
class Agriculture:
    def __init__(self, start_year):
        self = self
        self.start_year = start_year
        
        self.AL     = CONST.INITIAL.ALI
        self.PAL    = CONST.INITIAL.PALI
        self.UIL    = CONST.INITIAL.UILI
        self.LFERT  = CONST.INITIAL.LFERTI
        self.AI     = CONST.INITIAL.AII
        self.PFR    = CONST.INITIAL.PFRI
        
    def initial_result(self):
        ret = {}
        ret[CONST.RETURNS.AI]       = CONST.INITIAL.AII
        ret[CONST.RETURNS.F]        = CONST.INITIAL.FI
        ret[CONST.RETURNS.FALM]     = CONST.INITIAL.FALMI
        ret[CONST.RETURNS.FIOAA]    = CONST.INITIAL.FIOAAI
        return ret    
    
    def model(self,  
                 current_year, 
                 io, pop, ppolx,
                 year_step = CONST.YEAR_STEP_SIZE):
        
        FALM = f.f126(self.PFR)
        AIPH = self.AI * (1 - FALM) / self.AL
        LY = self.LFERT * f.f102(AIPH) * f.f106(io)
        F = LY * self.AL * 0.63
        FPC = F / pop
        IFPC = f.f90(io/pop)
        FIOAA = f.f94(FPC/IFPC)
        TAI = FIOAA * io
        DCPH = f.f97(self.PAL/3.2*10**9)
        MPLD = LY / (DCPH * 0.7)
        MPAI = 2 * LY * f.f111(AIPH) / f.f102(AIPH)
        FIALD = f.f108(MPLD / MPAI)
        
        CAI = TAI * (1 - FIALD)
        FR = FPC / 230
        LFDR = f.f122(ppolx)
        LFRT = f.f125(FALM)
        LER = self.AL / (6000*f.f114(LY/600)) 
        LRUI = max(0, (pop/f.f117(io/pop) - self.UIL)/10)
        LDR = FIALD * TAI / DCPH
        
        dAL = LDR - LRUI - LER
        dPAL = -1 * LDR
        dUIL = LRUI
        dLFERT = (600 - self.LFERT)/LFRT - self.LFERT*LFDR
        dAI = (CAI - self.AI)/2
        dPFR = (FR - self.PFR)/2
        
        
        self.AL += (dAL * year_step)
        self.PAL += (dPAL * year_step)
        self.UIL += (dUIL * year_step)
        self.LFERT += (dLFERT * year_step)
        self.AI += (dAI * year_step)
        self.PFR += (dPFR * year_step)
        
        ret = {}
        ret[CONST.RETURNS.AI] = self.AI
        ret[CONST.RETURNS.F] = F
        ret[CONST.RETURNS.FALM] = FALM
        ret[CONST.RETURNS.FIOAA] = FIOAA
        return ret

