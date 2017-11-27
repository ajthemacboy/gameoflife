from PyQt5 import QtCore, QtGui, QtWidgets
from version03_layout import Ui_MainWindow
import sys, os, pickle


class WINDOW(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.defaults = {
                "listB": [3],
                "listS": [2, 3],
                "sliderFPSVal": 15,
                "sliderUpdateVal": 5,
                "sliderCellSizeVal": 16,
                "boxXVal": 48,
                "boxYVal": 48,
                "boxPaddingVal": 16,
                "boxSparsityVal": 4,
                "checkStartPausedVal": False
            }

        if os.path.exists("config/config.pkl"):                                                                         # If config file exists, load it
            with open("config/config.pkl", "rb") as f:
                self.config = pickle.load(f)

            self.updateMenu()

        else:                                                                                                           # If it doesn't, create the dictionary
            self.config = self.defaults

        self.graceful = False

        self.labelFPSVal.setText(str(self.sliderFPS.value()))
        self.labelUpdateVal.setText(str(self.sliderUpdate.value()))
        self.labelCellSizeVal.setText(str(self.sliderCellSize.value()))

        self.buttonGo.clicked.connect(self.inputEvent)
        self.buttonReset.clicked.connect(self.inputEvent)
        self.sliderFPS.valueChanged.connect(self.inputEvent)                                                            # Sliders update value labels next to them
        self.sliderUpdate.valueChanged.connect(self.inputEvent)
        self.sliderCellSize.valueChanged.connect(self.inputEvent)

    def updateMenu(self):

        self.B0.setChecked(True) if 0 in self.config["listB"] else self.B0.setChecked(False)                            # Reset checkboxes
        self.B1.setChecked(True) if 1 in self.config["listB"] else self.B1.setChecked(False)
        self.B2.setChecked(True) if 2 in self.config["listB"] else self.B2.setChecked(False)
        self.B3.setChecked(True) if 3 in self.config["listB"] else self.B3.setChecked(False)
        self.B4.setChecked(True) if 4 in self.config["listB"] else self.B4.setChecked(False)
        self.B5.setChecked(True) if 5 in self.config["listB"] else self.B5.setChecked(False)
        self.B6.setChecked(True) if 6 in self.config["listB"] else self.B6.setChecked(False)
        self.B7.setChecked(True) if 7 in self.config["listB"] else self.B7.setChecked(False)
        self.B8.setChecked(True) if 8 in self.config["listB"] else self.B8.setChecked(False)

        self.S0.setChecked(True) if 0 in self.config["listS"] else self.S0.setChecked(False)
        self.S1.setChecked(True) if 1 in self.config["listS"] else self.S1.setChecked(False)
        self.S2.setChecked(True) if 2 in self.config["listS"] else self.S2.setChecked(False)
        self.S3.setChecked(True) if 3 in self.config["listS"] else self.S3.setChecked(False)
        self.S4.setChecked(True) if 4 in self.config["listS"] else self.S4.setChecked(False)
        self.S5.setChecked(True) if 5 in self.config["listS"] else self.S5.setChecked(False)
        self.S6.setChecked(True) if 6 in self.config["listS"] else self.S6.setChecked(False)
        self.S7.setChecked(True) if 7 in self.config["listS"] else self.S7.setChecked(False)
        self.S8.setChecked(True) if 8 in self.config["listS"] else self.S8.setChecked(False)

        self.sliderFPS.setProperty("value", self.config["sliderFPSVal"])                                                # Reset other settings
        self.sliderUpdate.setProperty("value", self.config["sliderUpdateVal"])
        self.sliderCellSize.setProperty("value", self.config["sliderCellSizeVal"])
        self.boxX.setProperty("value", self.config["boxXVal"])
        self.boxY.setProperty("value", self.config["boxYVal"])
        self.boxPadding.setProperty("value", self.config["boxPaddingVal"])
        self.boxSparsity.setProperty("value", self.config["boxSparsityVal"])
        self.checkStartPaused.setChecked(self.config["checkStartPausedVal"])

    def inputEvent(self, value):
        sender = self.sender()

        if sender.objectName() == "buttonGo":
            self.config = self.defaults
            self.config["listB"] = []                                                                                   # Empty default list values; new values are appended, not overwritten
            self.config["listS"] = []

            if self.B0.isChecked(): self.config["listB"].append(0)                                                      # Save checkboxes
            if self.B1.isChecked(): self.config["listB"].append(1)
            if self.B2.isChecked(): self.config["listB"].append(2)
            if self.B3.isChecked(): self.config["listB"].append(3)
            if self.B4.isChecked(): self.config["listB"].append(4)
            if self.B5.isChecked(): self.config["listB"].append(5)
            if self.B6.isChecked(): self.config["listB"].append(6)
            if self.B7.isChecked(): self.config["listB"].append(7)
            if self.B8.isChecked(): self.config["listB"].append(8)

            if self.S0.isChecked(): self.config["listS"].append(0)
            if self.S1.isChecked(): self.config["listS"].append(1)
            if self.S2.isChecked(): self.config["listS"].append(2)
            if self.S3.isChecked(): self.config["listS"].append(3)
            if self.S4.isChecked(): self.config["listS"].append(4)
            if self.S5.isChecked(): self.config["listS"].append(5)
            if self.S6.isChecked(): self.config["listS"].append(6)
            if self.S7.isChecked(): self.config["listS"].append(7)
            if self.S8.isChecked(): self.config["listS"].append(8)

            self.config["sliderFPSVal"] = self.sliderFPS.value()                                                        # Save other settings
            self.config["sliderUpdateVal"] = self.sliderUpdate.value()
            self.config["sliderCellSizeVal"] = self.sliderCellSize.value()
            self.config["boxXVal"] = self.boxX.value()
            self.config["boxYVal"] = self.boxY.value()
            self.config["boxPaddingVal"] = self.boxPadding.value()
            self.config["boxSparsityVal"] = self.boxSparsity.value()
            self.config["checkStartPausedVal"] = self.checkStartPaused.isChecked()

            if not os.path.exists("config"):
                os.makedirs("config")
            with open("config/config.pkl", "wb") as f:
                pickle.dump(self.config, f, pickle.HIGHEST_PROTOCOL)

            self.graceful = True
            self.close()

        elif sender.objectName() == "buttonReset":
            self.config = self.defaults
            self.updateMenu()
        elif sender.objectName() == "sliderFPS":
            self.labelFPSVal.setText(str(self.sliderFPS.value()))
        elif sender.objectName() == "sliderUpdate":
            self.labelUpdateVal.setText(str(self.sliderUpdate.value()))
        elif sender.objectName() == "sliderCellSize":
            self.labelCellSizeVal.setText(str(self.sliderCellSize.value()))


def load():
    program = QtWidgets.QApplication(sys.argv)
    window = WINDOW()
    window.show()
    program.exec_()

    if not window.graceful:
        sys.exit()

    return (
            window.config["listB"],
            window.config["listS"],
            window.config["sliderFPSVal"],
            window.config["sliderUpdateVal"],
            window.config["sliderCellSizeVal"],
            window.config["boxXVal"],
            window.config["boxYVal"],
            window.config["boxPaddingVal"],
            window.config["boxSparsityVal"],
            window.config["checkStartPausedVal"]
            )
