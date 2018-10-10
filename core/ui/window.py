from PyQt5.QtWidgets import QMainWindow
from core.ui.menubar import LoadMenuBar
from core.ui.statusbar import LoadStatusBar
from core.ui.plot_ui import plot_widget
from core.ui.Integrated_Body import BodyWindow




class window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(50, 50, 800, 600)
        self.setMinimumSize(1200, 700)
        self.setWindowTitle('Arduino Control pannel')

        # MenuBar
        menu_bar = self.menuBar()
        menu_bar = LoadMenuBar(menu_bar)    #傳入menubar object 進行操作

        # Plot Window
        # plot_ui = plot_widget(self)
        # self.setCentralWidget(plot_ui)  # 填充剩下的位置
        # plot_ui.plot()     #讓arduino調用

        # Status Bar
        status_bar = self.statusBar()
        status_bar_obj = LoadStatusBar(status_bar)

        # select block
        Body = BodyWindow(self,status_bar_obj)
        self.setCentralWidget(Body)