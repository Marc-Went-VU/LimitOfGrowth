import numpy as np
import matplotlib.pyplot as plt
class Plot:
    def __init__(self, results):
        self.results = []
        if isinstance(results, list) and isinstance(results[0], list) and isinstance(results[0][0], list) :
            for i in range(len(results)):
                self.results.append(np.asanyarray(results[i]))
        else:
            self.results.append(np.asanyarray(results))
    
    def plot(self, subplot=True, x=0, y=[]):
        color = ['b', 'r', 'g', 'p']
        
        for j in range(len(self.results)):
            result = self.results[j]
            plt.figure(j)
            plt.figure(num=None, figsize=(10, 12), dpi=80, facecolor='w', edgecolor='k')
            if subplot:
                xAxis = result[:,x]
                for i in range(len(y)):
                    plt.subplot(len(y),1,i)
                    
                    yAxis = result[:,y[i]]
                    plt.plot(xAxis, yAxis, color[i%len(color)])
                    #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1, ncol=2, borderaxespad=0.)
               
            else:
#                 plt.figure(j)
#                 plt.figure(num=None, figsize=(10, 12), dpi=80, facecolor='w', edgecolor='k')
                for i in range(len(y)):
                    plt.plot(result[:,x], result[:,y[i]], color[i%len(color)])
                
        plt.show()
    