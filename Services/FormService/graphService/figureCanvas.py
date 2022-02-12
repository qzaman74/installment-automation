
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=None, height=None, dpi=None, label=None, label1=None, value=None, value1=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        # self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(label, label1, value, value1)

    def plot(self,label, label1, value, value1):

        x = np.array([value, value1])
        labels = [label, label1]
        ax = self.figure.add_subplot(111)

        ax.pie(x, labels=labels)
        self.draw()
