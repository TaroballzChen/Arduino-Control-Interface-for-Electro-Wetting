from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

class Action():
    def Exit(self):
        exit_action = "123245646"
        return exit_action



class LoadMenuBar(Action):
    def __init__(self,menubar):
        self.init_menu(menubar)

    def init_menu(self,menubar):
        # Menu Option
        file = menubar.addMenu("File")

        # Option's Action
        file.addAction(self.Exit())


    def OptionAddAction(self,Option,*ActionList):
        for action in ActionList:
            Option.addAction(action)