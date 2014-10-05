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
        
        self.delaydDIOPC={self.start_year: CONST.INITIAL.DIOPCI}
        self.delaydFCFPC={self.start_year: CONST.INITIAL.FCFPCI}
        self.delaydPLE={self.start_year: CONST.INITIAL.PLEI}

    def initial_result(self):
        ret = {}
        ret[CONST.RETURNS.POP] = CONST.INITIAL.POPI
        return ret 
    
    def model(self, current_year,
                  io, so, F, ppolx,
                  year_step= CONST.YEAR_STEP_SIZE
                  ):        
        IOPC = io/self.POP
        FIE = (IOPC - self.AIOPC)/self.AIOPC
        DCFS = 4*f.f41(FIE)*f.f39(self.DIOPC)
        DTF = DCFS*f.f36(self.PLE)
        FPC = F/self.POP
        LMC = 1 - f.f27(IOPC)*f.f26(self.POP)
        LE = 28. * f.f25(self.EHSPC) * f.f20(FPC/230) * f.f29(ppolx) * LMC
        MTF = 12*f.f34(LE)
        SOPC = so/self.POP
        FCAPC = SOPC * f.f48(MTF/DTF - 1)
        FCE = f.f45(self.FCFPC)
        TF = min(MTF, MTF*(1-FCE)+DTF*FCE)
        B = 0.21*self.POP*TF/30
        HSAPC = f.f21(SOPC)
        D = self.POP/LE 
        
        #RGP = (dPOP/POP)*1000 # (B-D)/POP*1000
        
        dPOP = B - D
        dEHSPC = (HSAPC - self.EHSPC)/20
        dAIOPC = (IOPC - self.AIOPC)/3
        
        self.delaydDIOPC[current_year + 20/year_step] = IOPC
        self.delaydFCFPC[current_year + 20/year_step] = FCAPC
        self.delaydPLE[current_year + 20/year_step] = LE
        
        dDIOPC = f.get_unprecise_index(self.delaydDIOPC, current_year)
        dFCFPC = f.get_unprecise_index(self.delaydFCFPC, current_year)
        dPLE = f.get_unprecise_index(self.delaydPLE, current_year)
        
        self.POP += (dPOP * year_step)
        self.EHSPC += (dEHSPC * year_step)
        self.AIOPC += (dAIOPC * year_step)
        self.DIOPC += (dDIOPC * year_step)
        self.FCFPC += (dFCFPC * year_step)
        self.PLE += (dPLE * year_step)
        
        ret = {}
        ret[CONST.RETURNS.POP] = self.POP
        return ret


    def run_model(self,
                  io,
                  so,
                  F,
                  ppolx,
                  start_year = CONST.START_YEAR, 
                  year_range = CONST.YEAR_RANGE, 
                  year_step = CONST.YEAR_STEP_SIZE,
                  ):
        
        results = []
        results.append(self.extended_population_model(current_year = start_year,
                                                      io = io,
                                                      so = so,
                                                      F = F,
                                                      ppolx = ppolx,
                                                      POP = CONST.INITIAL.POPI,
                                                      EHSPC = CONST.INITIAL.EHSPCI,
                                                      AIOPC = CONST.INITIAL.AIOPCI,
                                                      DIOPC = CONST.INITIAL.DIOPCI,
                                                      FCFPC = CONST.INITIAL.FCFPCI,
                                                      PLE = CONST.INITIAL.PLEI,
                                                      year_step = year_step,
                                                      delaydDIOPC={start_year: CONST.INITIAL.DIOPCI},
                                                      delaydFCFPC={start_year: CONST.INITIAL.FCFPCI},
                                                      delaydPLE={start_year: CONST.INITIAL.PLEI}
                                                 )
                       )
        
        for x in f.drange(start_year+1, start_year+year_range, year_step):
            last_result = results[-1]
            results.append(self.extended_population_model(current_year = x,
                                                          io = io,
                                                          so = so,
                                                          F = F,
                                                          ppolx = ppolx,
                                                          POP = last_result[CONST.POPULATION.POP],
                                                          EHSPC = last_result[CONST.POPULATION.EHSPC],
                                                          AIOPC = last_result[CONST.POPULATION.AIOPC],
                                                          DIOPC = last_result[CONST.POPULATION.DIOPC],
                                                          FCFPC = last_result[CONST.POPULATION.FCFPC],
                                                          PLE = last_result[CONST.POPULATION.PLE],
                                                          year_step = year_step,
                                                          delaydDIOPC=last_result[CONST.POPULATION.DELAYED_dDIOPC],
                                                          delaydFCFPC=last_result[CONST.POPULATION.DELAYED_dFCFPC],
                                                          delaydPLE=last_result[CONST.POPULATION.DELAYED_dPLE])
                           )
        return results
