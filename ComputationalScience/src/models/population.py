import func as f
from const import _Const
        
CONST = _Const()
class Population:
    def __init__(self):
        self = self
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
        
    def extended_population_model(self, current_year,
                                  POP, EHSPC, AIOPC, DIOPC, FCFPC, PLE,
                                  io, so, F, ppolx,
                                  delaydDIOPC, delaydFCFPC, delaydPLE,
                                  year_step= CONST.YEAR_STEP_SIZE
                                  ):        
        IOPC = io/POP
        FIE = (IOPC - AIOPC)/AIOPC
        DCFS = 4*f.f41(FIE)*f.f39(DIOPC)
        DTF = DCFS*f.f36(PLE)
        FPC = F/POP
        LMC = 1 - f.f27(IOPC)*f.f26(POP)
        LE = 28 * f.f25(EHSPC) * f.f20(FPC/230) * f.f29(ppolx) * LMC
        MTF = 12*f.f34(LE)
        SOPC = so/POP
        FCAPC = SOPC * f.f48(MTF/DTF - 1)
        FCE = f.f45(FCFPC)
        TF = min(MTF, MTF*(1-FCE)+DTF*FCE)
        B = 0.21*POP*TF/30
        HSAPC = f.f21(SOPC)
        D = POP/LE 
        
        #RGP = (dPOP/POP)*1000 # (B-D)/POP*1000
        
        dPOP = B - D
        dEHSPC = (HSAPC - EHSPC)/20
        dAIOPC = (IOPC - AIOPC)/3
        
        delaydDIOPC[current_year + 20/year_step] = IOPC
        delaydFCFPC[current_year + 20/year_step] = FCAPC
        delaydPLE[current_year + 20/year_step] = LE
        
        dDIOPC = f.get_unprecise_index(delaydDIOPC, current_year)
        dFCFPC = f.get_unprecise_index(delaydFCFPC, current_year)
        dPLE = f.get_unprecise_index(delaydPLE, current_year)
        
        POP += (dPOP * year_step)
        EHSPC += (dEHSPC * year_step)
        AIOPC += (dAIOPC * year_step)
        DIOPC += (dDIOPC * year_step)
        FCFPC += (dFCFPC * year_step)
        PLE += (dPLE * year_step)
        
        ret = [current_year]
        ret.insert(CONST.POPULATION.POP, POP)
        ret.insert(CONST.POPULATION.EHSPC, EHSPC)
        ret.insert(CONST.POPULATION.AIOPC, AIOPC)
        ret.insert(CONST.POPULATION.DIOPC, DIOPC)
        ret.insert(CONST.POPULATION.FCFPC, FCFPC)
        ret.insert(CONST.POPULATION.PLE, PLE)
        ret.insert(CONST.POPULATION.DELAYED_dDIOPC, delaydDIOPC)
        ret.insert(CONST.POPULATION.DELAYED_dFCFPC, delaydFCFPC)
        ret.insert(CONST.POPULATION.DELAYED_dPLE, delaydPLE)
        return ret

