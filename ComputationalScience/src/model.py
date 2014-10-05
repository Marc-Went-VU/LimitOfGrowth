from plot import Plot
import matplotlib.pyplot as plt
import collections
import func as f
from models.capital_extended import Capital
from models.population import Population
from models.pollution import Pollution
from models.agriculture import Agriculture
from const import _Const
CONST = _Const()


start_year = 1900
year_step = 1

capital     = Capital(CONST.START_YEAR)
population  = Population(CONST.START_YEAR)
pollution   = Pollution(CONST.START_YEAR)
agriculture = Agriculture(CONST.START_YEAR)

init_result = dict(capital.initial_result().items() + 
                   population.initial_result().items() + 
                   pollution.initial_result().items() + 
                   agriculture.initial_result().items())
results = [init_result]
result_dict = {}

population_list = {}
year_list = f.drange(CONST.START_YEAR, CONST.START_YEAR+CONST.YEAR_RANGE, CONST.YEAR_STEP_SIZE)
for x in year_list:
    last_result = results[-1]
    result_dict[x] = last_result
    population_list[x] = last_result[CONST.RETURNS.POP]
    cap_res = capital.model(current_year = x, 
                            fioaa       = last_result[CONST.RETURNS.FIOAA],
                            pop         = last_result[CONST.RETURNS.POP])
    
    pop_res = population.model(current_year = x,
                               io       = last_result[CONST.RETURNS.FIOAA],
                               so       = last_result[CONST.RETURNS.POP],
                               F        = last_result[CONST.RETURNS.F],
                               ppolx    = last_result[CONST.RETURNS.PPOLX])
    
    pol_res = pollution.model(current_year = x,
                              io        = last_result[CONST.RETURNS.IO],
                              pop       = last_result[CONST.RETURNS.POP],
                              falm      = last_result[CONST.RETURNS.FALM],
                              ai        = last_result[CONST.RETURNS.AI])
    
    arg_res = agriculture.model(current_year = x, 
                                io      = last_result[CONST.RETURNS.IO], 
                                pop     = last_result[CONST.RETURNS.POP],
                                ppolx   = last_result[CONST.RETURNS.PPOLX])
    result = dict(cap_res.items() + 
                   pop_res.items() +
                   pol_res.items() +
                   arg_res.items())
    results.append(result)


for key, value in sorted(population_list.items(), key=lambda x:x[1]):
    print "%s - %s " %(key, value)

#plt.plot(population_list)