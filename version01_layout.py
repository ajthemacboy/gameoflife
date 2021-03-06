from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.listB = []
        self.listS = []
        self.sliderFPSVal = 0
        self.sliderUpdateVal = 0
        self.boxXVal = 0
        self.boxYVal = 0
        self.boxPaddingVal = 0
        self.boxSparsityVal = 0

        self.MainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 261)
        MainWindow.setMinimumSize(QtCore.QSize(341, 261))
        MainWindow.setMaximumSize(QtCore.QSize(341, 261))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelHeader = QtWidgets.QLabel(self.centralwidget)
        self.labelHeader.setGeometry(QtCore.QRect(10, 10, 111, 20))
        self.labelHeader.setObjectName("labelHeader")

        self.buttonGo = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGo.setGeometry(QtCore.QRect(180, 200, 111, 23))
        self.buttonGo.setObjectName("buttonGo")
        self.buttonGo.clicked.connect(self.inputEvent)

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 31, 51, 222))
        self.layoutWidget.setObjectName("layoutWidget")

        self.layoutBirth = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layoutBirth.setContentsMargins(0, 0, 0, 0)
        self.layoutBirth.setObjectName("layoutBirth")

        self.birth = QtWidgets.QLabel(self.layoutWidget)
        self.birth.setObjectName("birth")
        self.layoutBirth.addWidget(self.birth)

        self.B0 = QtWidgets.QCheckBox(self.layoutWidget)
        self.B0.setObjectName("B0")
        self.layoutBirth.addWidget(self.B0, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.B1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.B1.setObjectName("B1")
        self.layoutBirth.addWidget(self.B1, 0, QtCore.Qt.AlignHCenter)

        self.B2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.B2.setObjectName("B2")
        self.layoutBirth.addWidget(self.B2, 0, QtCore.Qt.AlignHCenter)

        self.B3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.B3.setChecked(True)
        self.B3.setObjectName("B3")
        self.layoutBirth.addWidget(self.B3, 0, QtCore.Qt.AlignHCenter)

        self.B4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.B4.setObjectName("B4")
        self.layoutBirth.addWidget(self.B4, 0, QtCore.Qt.AlignHCenter)

        self.B5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.B5.setObjectName("B5")
        self.layoutBirth.addWidget(self.B5, 0, QtCore.Qt.AlignHCenter)

        self.B6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.B6.setObjectName("B6")
        self.layoutBirth.addWidget(self.B6, 0, QtCore.Qt.AlignHCenter)

        self.B7 = QtWidgets.QCheckBox(self.layoutWidget)
        self.B7.setObjectName("B7")
        self.layoutBirth.addWidget(self.B7, 0, QtCore.Qt.AlignHCenter)

        self.B8 = QtWidgets.QCheckBox(self.layoutWidget)
        self.B8.setObjectName("B8")
        self.layoutBirth.addWidget(self.B8, 0, QtCore.Qt.AlignHCenter)

        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 31, 51, 222))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.layoutSurvival = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.layoutSurvival.setContentsMargins(0, 0, 0, 0)
        self.layoutSurvival.setObjectName("layoutSurvival")

        self.survival = QtWidgets.QLabel(self.layoutWidget1)
        self.survival.setObjectName("survival")
        self.layoutSurvival.addWidget(self.survival)

        self.S0 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.S0.setObjectName("S0")
        self.layoutSurvival.addWidget(self.S0, 0, QtCore.Qt.AlignHCenter)

        self.S1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.S1.setObjectName("S1")
        self.layoutSurvival.addWidget(self.S1, 0, QtCore.Qt.AlignHCenter)

        self.S2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.S2.setChecked(True)
        self.S2.setObjectName("S2")
        self.layoutSurvival.addWidget(self.S2, 0, QtCore.Qt.AlignHCenter)

        self.S3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.S3.setChecked(True)
        self.S3.setObjectName("S3")
        self.layoutSurvival.addWidget(self.S3, 0, QtCore.Qt.AlignHCenter)

        self.S4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.S4.setObjectName("S4")
        self.layoutSurvival.addWidget(self.S4, 0, QtCore.Qt.AlignHCenter)

        self.S5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.S5.setObjectName("S5")
        self.layoutSurvival.addWidget(self.S5, 0, QtCore.Qt.AlignHCenter)

        self.S6 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.S6.setObjectName("S6")
        self.layoutSurvival.addWidget(self.S6, 0, QtCore.Qt.AlignHCenter)

        self.S7 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.S7.setObjectName("S7")
        self.layoutSurvival.addWidget(self.S7, 0, QtCore.Qt.AlignHCenter)

        self.S8 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.S8.setObjectName("S8")
        self.layoutSurvival.addWidget(self.S8, 0, QtCore.Qt.AlignHCenter)

        self.sliderFPS = QtWidgets.QSlider(self.centralwidget)
        self.sliderFPS.setGeometry(QtCore.QRect(140, 50, 191, 22))
        self.sliderFPS.setMinimum(1)
        self.sliderFPS.setMaximum(150)
        self.sliderFPS.setSingleStep(1)
        self.sliderFPS.setProperty("value", 15)
        self.sliderFPS.setOrientation(QtCore.Qt.Horizontal)
        self.sliderFPS.setObjectName("sliderFPS")

        self.labelFPS = QtWidgets.QLabel(self.centralwidget)
        self.labelFPS.setGeometry(QtCore.QRect(140, 30, 47, 13))
        self.labelFPS.setObjectName("labelFPS")

        self.sliderUpdate = QtWidgets.QSlider(self.centralwidget)
        self.sliderUpdate.setGeometry(QtCore.QRect(140, 100, 191, 22))
        self.sliderUpdate.setMinimum(1)
        self.sliderUpdate.setMaximum(100)
        self.sliderUpdate.setProperty("value", 5)
        self.sliderUpdate.setOrientation(QtCore.Qt.Horizontal)
        self.sliderUpdate.setObjectName("sliderUpdate")

        self.labelUpdate = QtWidgets.QLabel(self.centralwidget)
        self.labelUpdate.setGeometry(QtCore.QRect(140, 80, 81, 16))
        self.labelUpdate.setObjectName("labelUpdate")

        self.boxX = QtWidgets.QSpinBox(self.centralwidget)
        self.boxX.setGeometry(QtCore.QRect(140, 150, 42, 22))
        self.boxX.setMinimum(1)
        self.boxX.setMaximum(100)
        self.boxX.setProperty("value", 48)
        self.boxX.setObjectName("boxX")

        self.boxY = QtWidgets.QSpinBox(self.centralwidget)
        self.boxY.setGeometry(QtCore.QRect(190, 150, 42, 22))
        self.boxY.setMinimum(1)
        self.boxY.setMaximum(100)
        self.boxY.setProperty("value", 48)
        self.boxY.setObjectName("boxY")

        self.labelX = QtWidgets.QLabel(self.centralwidget)
        self.labelX.setGeometry(QtCore.QRect(140, 130, 16, 16))
        self.labelX.setObjectName("labelX")

        self.labelY = QtWidgets.QLabel(self.centralwidget)
        self.labelY.setGeometry(QtCore.QRect(190, 130, 16, 16))
        self.labelY.setObjectName("labelY")

        self.boxPadding = QtWidgets.QSpinBox(self.centralwidget)
        self.boxPadding.setGeometry(QtCore.QRect(240, 150, 42, 22))
        self.boxPadding.setProperty("value", 12)
        self.boxPadding.setObjectName("boxPadding")

        self.labelPadding = QtWidgets.QLabel(self.centralwidget)
        self.labelPadding.setGeometry(QtCore.QRect(240, 130, 47, 13))
        self.labelPadding.setObjectName("labelPadding")

        self.boxSparsity = QtWidgets.QSpinBox(self.centralwidget)
        self.boxSparsity.setGeometry(QtCore.QRect(290, 150, 42, 22))
        self.boxSparsity.setMinimum(1)
        self.boxSparsity.setMaximum(100)
        self.boxSparsity.setProperty("value", 4)
        self.boxSparsity.setObjectName("boxSparsity")

        self.labelSparsity = QtWidgets.QLabel(self.centralwidget)
        self.labelSparsity.setGeometry(QtCore.QRect(290, 130, 47, 13))
        self.labelSparsity.setObjectName("labelSparsity")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelHeader.setText(_translate("MainWindow",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Game of Life Rules</span></p></body></html>"))
        self.buttonGo.setText(_translate("MainWindow", "Go"))
        self.birth.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Birth</p></body></html>"))
        self.B0.setText(_translate("MainWindow", "0"))
        self.B1.setText(_translate("MainWindow", "1"))
        self.B2.setText(_translate("MainWindow", "2"))
        self.B3.setText(_translate("MainWindow", "3"))
        self.B4.setText(_translate("MainWindow", "4"))
        self.B5.setText(_translate("MainWindow", "5"))
        self.B6.setText(_translate("MainWindow", "6"))
        self.B7.setText(_translate("MainWindow", "7"))
        self.B8.setText(_translate("MainWindow", "8"))
        self.survival.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Survival</p></body></html>"))
        self.S0.setText(_translate("MainWindow", "0"))
        self.S1.setText(_translate("MainWindow", "1"))
        self.S2.setText(_translate("MainWindow", "2"))
        self.S3.setText(_translate("MainWindow", "3"))
        self.S4.setText(_translate("MainWindow", "4"))
        self.S5.setText(_translate("MainWindow", "5"))
        self.S6.setText(_translate("MainWindow", "6"))
        self.S7.setText(_translate("MainWindow", "7"))
        self.S8.setText(_translate("MainWindow", "8"))
        self.labelFPS.setText(_translate("MainWindow", "Max FPS"))
        self.labelUpdate.setText(_translate("MainWindow", "Update interval"))
        self.labelX.setText(_translate("MainWindow", "<html><head/><body><p>X</p></body></html>"))
        self.labelY.setText(_translate("MainWindow", "<html><head/><body><p>Y</p></body></html>"))
        self.labelPadding.setText(_translate("MainWindow", "Padding"))
        self.labelSparsity.setText(_translate("MainWindow", "Sparsity"))

    def inputEvent(self, value):

        sender = self.MainWindow.sender()

        if sender.objectName() == "buttonGo":

            if self.B0.isChecked(): self.listB.append(0)
            if self.B1.isChecked(): self.listB.append(1)
            if self.B2.isChecked(): self.listB.append(2)
            if self.B3.isChecked(): self.listB.append(3)
            if self.B4.isChecked(): self.listB.append(4)
            if self.B5.isChecked(): self.listB.append(5)
            if self.B6.isChecked(): self.listB.append(6)
            if self.B7.isChecked(): self.listB.append(7)
            if self.B8.isChecked(): self.listB.append(8)

            if self.S0.isChecked(): self.listS.append(0)
            if self.S1.isChecked(): self.listS.append(1)
            if self.S2.isChecked(): self.listS.append(2)
            if self.S3.isChecked(): self.listS.append(3)
            if self.S4.isChecked(): self.listS.append(4)
            if self.S5.isChecked(): self.listS.append(5)
            if self.S6.isChecked(): self.listS.append(6)
            if self.S7.isChecked(): self.listS.append(7)
            if self.S8.isChecked(): self.listS.append(8)

            self.sliderFPSVal = self.sliderFPS.value()
            self.sliderUpdateVal = self.sliderUpdate.value()
            self.boxXVal = self.boxX.value()
            self.boxYVal = self.boxY.value()
            self.boxPaddingVal = self.boxPadding.value()
            self.boxSparsityVal = self.boxSparsity.value()

            self.close()


class RULES(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


def launchRules():
    ruleGUI = QtWidgets.QApplication(sys.argv)
    rules = RULES()
    rules.show()
    ruleGUI.exec_()

    if not rules.listB and not rules.listS:  # If the checkbox values never populated, we know "Go" was not clicked
        sys.exit()

    return (rules.listB, rules.listS, rules.sliderFPSVal, rules.sliderUpdateVal, rules.boxXVal, rules.boxYVal,
            rules.boxPaddingVal, rules.boxSparsityVal)
