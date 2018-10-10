from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class plot_widget(FigureCanvas):
    def __init__(self, parent = None,width=23.5,height=4,dpi=100):
        self.figure = plt.figure(figsize=(width,height),dpi=dpi)
        FigureCanvas.__init__(self, self.figure)
        self.setParent(parent)
        self.toolbar = NavigationToolbar(self,self)
        self.move(-230,600)
        self.toolbar.move(230,-5)

    def plot(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.set(ylabel=r'signal (a.u.)',xlabel = "time (sec.)")
        ax.set_ylim(auto=True)
        ax.set_xlim(auto=True)

        ax.legend(loc='upper left')
        self.draw()

