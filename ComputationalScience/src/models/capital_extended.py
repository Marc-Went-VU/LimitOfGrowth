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
                                                     nr = last_result[CONST.NR], 
                                                     ic = last_result[CONST.IC], 
                                                     sc = last_result[CONST.SC],
                                                     year_step = year_step)
                           )
        return results
        
    def extended_captial_model(self,  
                             current_year, 
                             fioaa,
                             pop, 
                             nr, 
                             ic, 
                             sc,
                             year_step = CONST.YEAR_STEP_SIZE):
        ALIC = 14
        ALSC = 20
        FIOAC = 0.43
        ICOR = 3
        NRUF = 1
        SCOR = 1
        CUF = 1
        
        NRFR = nr / CONST.INITIAL.NRI
        FCAOR = f.f135(NRFR)
        IO = ic * CUF * (1 - FCAOR) / ICOR
        IOPC = IO / pop
        ISOPC = f.f61(IOPC)
        PCRUM = f.f132(IOPC)
        SO = sc * CUF / SCOR
        SOPC = SO/ pop
        FIOAS = f.f64(IOPC)
        U = 1 - FIOAC - fioaa
        FIOAI = U - FIOAS
            
        dIC = FIOAI * IO - ic/ALIC
        dSC = FIOAS * IO - sc/ALSC
        dNR = -1 * NRUF * PCRUM * pop
        
        nr += (dNR * year_step)
        ic += (dIC * year_step)
        sc += (dSC * year_step)
        ret = [current_year]
        ret.insert(CONST.NR, nr)
        ret.insert(CONST.IC, ic)
        ret.insert(CONST.SC, sc)
        return ret

