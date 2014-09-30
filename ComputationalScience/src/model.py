from plot import Plot
from models.capital_simple import Capital
from models.population import Population
from const import _Const
CONST = _Const()
Capital = Capital()
Population = Population()

result = Population.run_model(start_year=1900, 
                     year_range=200, 
                     year_step=0.5,
                     io = CONST.INITIAL.IOI,
                     so = CONST.INITIAL.SOI,
                     F = CONST.INITIAL.FI,
                     ppolx = CONST.INITIAL.PPOLXI
                    )

# result = Capital.run_model(start_year=1900, 
#                             year_range=200, 
#                             year_step=0.5, 
#                             fioaa=0.05, 
#                             nri=CONST.NRI, 
#                             ici=CONST.ICI, 
#                             sci=CONST.SCI)
# plot = Plot(result)
# plot.plot(subplot=True, x = CONST.CAPITAL.YEAR, y=[CONST.CAPITAL.NR, CONST.CAPITAL.IC, CONST.CAPITAL.SC])
print result