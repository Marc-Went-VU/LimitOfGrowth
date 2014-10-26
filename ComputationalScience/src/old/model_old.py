from plot_old import Plot
from capital_simple_old import Capital
from const_old import _Const
CONST = _Const()
Capital = Capital()


result = Capital.run_model(start_year=1900, 
                            year_range=200, 
                            year_step=0.5, 
                            fioaa=0.05, 
                            nri=CONST.INITIAL.NRI, 
                            ici=CONST.INITIAL.ICI, 
                            sci=CONST.INITIAL.SCI)
plot = Plot(result)
plot.plot(subplot=True, x = CONST.CAPITAL.YEAR, y=[CONST.CAPITAL.NR, CONST.CAPITAL.IC, CONST.CAPITAL.SC])
print result