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
        
    def initial_result(self):
        ret = {}
        ret[CONST.RETURNS.IO] = CONST.INITIAL.IOI
        ret[CONST.RETURNS.SO] = CONST.INITIAL.SOI
        
        
        ret[CONST.RETURNS.IC] = CONST.INITIAL.ICI
        ret[CONST.RETURNS.NR] = CONST.INITIAL.NRI
        ret[CONST.RETURNS.SC] = CONST.INITIAL.SCI
        return ret
    
    def model(self,  
                 current_year, 
                 fioaa, pop, 
                 year_step = CONST.YEAR_STEP_SIZE):
        ALIC = 14
        ALSC = 20
        FIOAC = 0.43
        ICOR = 3
        NRUF = 1
        SCOR = 1
        CUF = 1
        
        NRFR = self.NR / CONST.INITIAL.NRI
        FCAOR = f.f135(NRFR)
        IO = self.IC * CUF * (1 - FCAOR) / ICOR
        IOPC = IO / pop
        ISOPC = f.f61(IOPC)
        PCRUM = f.f132(IOPC)
        SO = self.SC * CUF / SCOR
        SOPC = SO / pop
        FIOAS = f.f64(IOPC)
        U = 1 - FIOAC - fioaa
        FIOAI = U - FIOAS
            
        dIC = FIOAI * IO - self.IC/ALIC
        dSC = FIOAS * IO - self.SC/ALSC
        dNR = -1 * NRUF * PCRUM * pop
        
        self.NR += (dNR * year_step)
        self.IC += (dIC * year_step)
        self.SC += (dSC * year_step)
        
        ret = {}
        ret[CONST.RETURNS.IO] = IO
        ret[CONST.RETURNS.SO] = SO
        
        ret[CONST.RETURNS.IC] = self.IC
        ret[CONST.RETURNS.NR] = self.NR
        ret[CONST.RETURNS.SC] = self.SC
        return ret
