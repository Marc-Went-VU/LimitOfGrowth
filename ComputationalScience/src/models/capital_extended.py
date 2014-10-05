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
        IO = self.IC* CUF * (1 - FCAOR) / ICOR
        IOPC = IO / pop
        ISOPC = f.f61(IOPC)
        PCRUM = f.f132(IOPC)
        SO = self.SC * CUF / SCOR
        SOPC = SO/ pop
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
        return ret

    def run_model(self, 
                  start_year = CONST.START_YEAR, 
                  year_range = CONST.YEAR_RANGE, 
                  year_step = CONST.YEAR_STEP_SIZE,
                  fioaa = CONST.FIOAA):
        
        results = []
        results.append(self.extended_captial_model(current_year = start_year, 
                                                 fioaa = fioaa, 
                                                 pop = CONST.INITIAL.POPI,
                                                 nr = CONST.INITIAL.NRI, 
                                                 ic = CONST.INITIAL.ICI, 
                                                 sc = CONST.INITIAL.NRI,
                                                 year_step = year_step,
                                                 nri = CONST.INITIAL.NRI))
        
        for x in f.drange(start_year+1, start_year+year_range, year_step):
            last_result = results[-1]
            results.append(self.extended_captial_model(current_year = x, 
                                                     fioaa = fioaa,
                                                     pop = CONST.INITIAL.POPI,
                                                     nr = last_result[CONST.CAPITAL.NR], 
                                                     ic = last_result[CONST.CAPITAL.IC], 
                                                     sc = last_result[CONST.CAPITAL.SC],
                                                     year_step = year_step)
                           )
        return results
        
